# Isaac Krementsov
# 3/15/2020
# Introduction to Systems Engineering
# Flask LED Control - Controls two LED circuits through a Flask GUI
# This program allows the blinking LEDs feature - this code is on lines 31-87

import time
import threading
import RPi.GPIO as GPIO
from flask import Flask, render_template, request


# Set constants for the GPIO pins where the red LED and yellow LED circuits are plugged in
RED_PIN = 14
YELLOW_PIN = 23

# Use the Broadcom Model layout
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup the red and yellow circuits for power outputs
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)


# Initialize a new Flask web app, and create an empty variable for a thread to run alongside it
app = Flask(__name__)
parallel_thread = None


# BLINKING LED CODE BELOW

# Function to blink the red and yellow LEDs in an alternating pattern
def alternate_leds(red_pin, yellow_pin):
    # Save a reference to the parallel thread this function is running on
    this_thread = threading.currentThread()

    # Continuously check whether the thread is told to stop running
    while getattr(this_thread, "continue_running", True):
        # If the thread can continue, wait 1/4 second between alternating the power for each light

        time.sleep(0.25)

        GPIO.output(red_pin, GPIO.HIGH)
        GPIO.output(yellow_pin, GPIO.LOW)

        time.sleep(0.25)

        GPIO.output(red_pin, GPIO.LOW)
        GPIO.output(yellow_pin, GPIO.HIGH)

    # When the loop is told to exit, it will complete its cycle, leaving the yellow light on
    GPIO.output(yellow_pin, GPIO.LOW)


# Accept a POST HTTP request from the frontend interface to blink the LED
@app.route('/led_blink', methods=['POST'])
def led_blink():
    # Make sure we're referencing the global thread variable, instead of creating a new one reserved to this function
    global parallel_thread

    # Use the threading module to create a new thread that will not interrupt the Flask server process, using the alternate_leds function and passing parameters
    parallel_thread = threading.Thread(target=alternate_leds, kwargs={'red_pin': RED_PIN, 'yellow_pin': YELLOW_PIN})

    # Once the thread is started, the request can be closed without stopping the blinking process, which prevents a connection timeout
    parallel_thread.start()

    return "ok"


# Accept a POST HTTP request to stop blinking the LEDs
@app.route('/led_blink_off', methods=['POST'])
def led_blink_off():
    # Make sure we're referencing the global thread variable, instead of creating a new one reserved to this function
    global parallel_thread

    # Make sure the parallel thread has been initialized
    if parallel_thread is not None:
        # Tell the thread to stop continue running - this change will be detected in alternate_leds
        parallel_thread.continue_running = False

        # Once the thread stops, join it back to the main process
        parallel_thread.join()

    return "ok"

# (END OF BLINKING CODE)


# Accept a POST HTTP request to turn one of the LEDs on
@app.route('/led_on', methods=['POST'])
def led_on():
    # Get the request query parameter "color" to target a particular LED
    color = request.values.get('color')

    # Depending on the color requested, set a high power to a particular LED
    if color == 'Red':
        GPIO.output(RED_PIN, GPIO.HIGH)
    elif color == 'Yellow':
        GPIO.output(YELLOW_PIN, GPIO.HIGH)

    return 'ok'


# Accept a POST HTTP request to turn one of the LEDs off
@app.route('/led_off', methods=['POST'])
def led_off():
    # Get the request query parameter "color" to target a particular LED
    color = request.values.get('color')

    # Depending on the color requested, set a high power to a particular LED
    if color == 'Red':
        GPIO.output(RED_PIN, GPIO.LOW)
    elif color == 'Yellow':
        GPIO.output(YELLOW_PIN, GPIO.LOW)

    return 'ok'


# Serve the user interface page to the root URL
@app.route('/', methods=['GET'])
def home():
    # Render the page with a title and my name
    return render_template('button.html', title='Button', name='Isaac Krementsov')
