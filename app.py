import time
import threading
import RPi.GPIO as GPIO
from flask import Flask, render_template, request


RED_PIN = 14
YELLOW_PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)


app = Flask(__name__)
parallel_thread = None


def alternate_leds(red_pin, yellow_pin):
    this_thread = threading.currentThread()

    while getattr(this_thread, "continue_running", True):
        time.sleep(0.25)
        
        GPIO.output(red_pin, GPIO.HIGH)
        GPIO.output(yellow_pin, GPIO.LOW)

        time.sleep(0.25)

        GPIO.output(red_pin, GPIO.LOW)
        GPIO.output(yellow_pin, GPIO.HIGH)

    GPIO.output(yellow_pin, GPIO.LOW)
        

@app.route('/led_blink', methods=['POST'])
def led_blink():
    global parallel_thread
    parallel_thread = threading.Thread(target=alternate_leds, kwargs={'red_pin': RED_PIN, 'yellow_pin': YELLOW_PIN})
    parallel_thread.start()
    
    return "ok"


@app.route('/led_blink_off', methods=['POST'])
def led_blink_off():
    global parallel_thread
    
    if parallel_thread is not None:
        parallel_thread.continue_running = False
        parallel_thread.join()

    return "ok"


@app.route('/led_on', methods=['POST'])
def led_on():
    color = request.values.get('color')

    if color == 'Red':
        GPIO.output(RED_PIN, GPIO.HIGH)
    elif color == 'Yellow':
        GPIO.output(YELLOW_PIN, GPIO.HIGH)

    return 'ok'


@app.route('/led_off', methods=['POST'])
def led_off():
    color = request.values.get('color')

    if color == 'Red':
        GPIO.output(RED_PIN, GPIO.LOW)
    elif color == 'Yellow':
        GPIO.output(YELLOW_PIN, GPIO.LOW)

    return 'ok'


@app.route('/', methods=['GET'])
def home():
    return render_template('button.html', title='Button', name='Isaac Krementsov')
