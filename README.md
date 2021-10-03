# SleepTight: HackOn2.0 Sleep Tracker Arduino Hardware hack - By Sriram and Vijay
<i>An innovative hardware solution to the sleeptracker. Sleep is important for your mental health; but phones are not! :')</i>

* This hardware solution sleep tracker is your go-to as it works without constant need for <i title="nor radiation">interaction</i> as with your smartphone apps
* It detects when the user is inside or outside the room via the **flex sensor** (placed on door so detects accordingly)
* It also detects when the room is dark (lights off) using the **photovoltaic cell**
* Using these sensors and some creative logic, it detects when the user is asleep based on a pre-determined sleep time and tracks your sleep
* Youtube Video: https://youtu.be/_t1lnJx8M5g


### The Vision
In today's day-and-age, with the current pandemic circumstances, an electronic gadget is probably more used than some inherent body parts! Why take it to sleep as well?
Did you know that smartphone radiation can have serious mental effects?! We'll leave you to research on that but going on to a more proven point, excessive smartphone use ruins your sleep cycle. Each sleep stage plays a part in allowing your mind and body to wake up refreshed. Understanding the sleep cycle also helps explain how certain sleep disorders, including insomnia and obstructive sleep apnea can impact a person's sleep and health. This brings us to the need of this product and why we sought to build it.

Current smartphone sleep tracker apps are really annoying. All of them either <i title="*ahem ahem* <enter major tech company>">steal all your data</i> or require you to do all the work. When we seek to reduce smartphone use at least during sleep, these make it impossible. Apart from that, studies show that the serious mental issues from the isolation are drastically visible in sleep and can include anxiety, anger management issues etc. We sought to fix that as well. The flex sensor doubles down as an anger management tool as well (it beeps until the flex is brought down to a certain range; this can be only done when calm and composed and hence seeks to calm the user) and the light sensor works as a handy night-lamp (blue light, ooooh!). 

Our aim was to make a hardware solution that could be easy-to-use ((just place it near the door) and maybe open the website once-a-day to check how your sleep cycle is going),  is multipurpose (and solves all directly correlated issues), targets and helps a wider audience, and <i title="most importantly (for us)">lastly</i>, was fun to work with! ¯\_(ツ)_/¯


### The Stack
This was built using `Arduino Uno (C++)`, `Python (Flask)`, `HTML5`, `CSS3`, `Javascript (jQuery)`, and `Excel` among others. It comes with a dedicated website that shows you the current sleep state and for the more eager user, it also produces a `.csv` file that can be graphed on Excel to collata sensor data. The website currently is just a prototype due to time constraints but we hope to add some better UI/UX design and aesthetics in the future!


### Instructions
1. Recreate the circuit using:
    1. the Arduino Uno microcontroller
    2. Modular Breadboard(s)
    3. Photovoltaic cell
    4. Flex sensor
    5. 3mm LEDs
    6. Buzzer
    7. Resistors (10kΩ for flex sensor; 330Ω for everything else) 
    8. and jumper cable 
    They can be connected as shown in the <a href="https://drive.google.com/drive/folders/1-8gYy0IJmczXpmyNJy44GIxhh6FLYi7Y?usp=sharing" target="_blank">Google Drive link</a>

2. Install all dependencies (`flask`, `pyserial`, `Arduino IDE`, etc.)
3. Connect USB from microcontroller to PC and upload Arduino code
4. Run the Flask application making sure to update the `.env` to correct `ARDUINO_PORT`

### The Team
Sriram N. V. and Vijay Anantha Padmanabhan are glad to have been able to work on this and hope you like it! ❤
