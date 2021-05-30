from flask import Flask, render_template, jsonify
from arduino import arduino
from time import sleep
from datetime import datetime

# set up Flask app
app = Flask(__name__)
flag = True
states = ["inside", "outside", "asleep"]
state = states[0]
sleep_start = datetime.utcnow().time()
sleep_end = False

# set up routes
@app.route("/")
def index():
    data = arduino(states, state, sleep_start, sleep_end)
    return render_template("index.html", data=data)


@app.route("/ret", methods=["POST", "GET"])
def ret():
    data = arduino(states, state, sleep_start, sleep_end)
    sleep(1)
    return jsonify(data)