from dotenv import load_dotenv
import os
from datetime import datetime, time
import serial
from serial.serialutil import SerialException
import csv

# load .env variables onto os.environ
load_dotenv()


def is_sleeptime(input_time):
    begin_time = time(22, 0)
    end_time = time(4, 0)
    # If check time is not given, default to current UTC time
    check_time = input_time or datetime.utcnow().time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else:  # crosses midnight
        return check_time >= begin_time or check_time <= end_time


def update_state(flex, light, states, state, sleep_start, sleep_end):
    # outside + switch = inside
    if (state == states[1]) and (flex <= int(os.environ.get("MIN_FLEX"))):
        state = states[0]

    # asleep + switch = awake
    elif state == states[2] and (flex <= int(os.environ.get("MIN_FLEX"))):
        state = states[0]
        sleep_end = datetime.utcnow().time()

    # is sleeping time (night)
    elif is_sleeptime(datetime.utcnow().time()):
        # sleep time + dark = asleep
        if (state == states[0]) and (light <= int(os.environ.get("MIN_LIGHT"))):
            state = states[2]
            sleep_start = datetime.utcnow().time()
            sleep_end = False
    else:
        # inside + switch = outside
        if (state == states[0]) and (flex <= int(os.environ.get("MIN_FLEX"))):
            state = states[1]


def arduino(states, state, sleep_start, sleep_end):
    flag = True
    # set up basic port and file config
    arduino_port = os.environ.get("ARDUINO_PORT")  # serial port of Arduino
    baud = os.environ.get("BAUD")  # arduino uno runs at 9600 baud
    fileName = "sleepTracker.csv"

    # connect to arduino and file
    try:
        ser = serial.Serial(arduino_port, baud)
    except SerialException:
        return True

    print("Connected to Arduino port:" + arduino_port)

    i = 0
    while i <= 100:
        with open(fileName, "a") as file:
            csvwriter = csv.writer(file, delimiter=",")
            # display the data to the terminal
            getData = str(ser.readline().decode("utf-8"))
            data = getData[0:][:-2].split(",")
            print(data)
            flex = int(data[0])
            light = int(data[1])
            i += 1
            # add the data to the file
            csvwriter.writerow([light, flex])  # write data with a newline

    update_state(flex, light, states, state, sleep_start, sleep_end)
    if state == states[2]:
        return "user is outside"
    elif state == states[0]:
        return f"Deep sleep since {sleep_start}"
    else:
        return "user is inside"
