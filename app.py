#import RPi.GPIO as GPIO
from flask import Flask, render_template, request


RED_PIN = 14
YELLOW_PIN = 23


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)


app = Flask(__name__)


@app.route('/led_on/:color', methods=['POST'])
def led_on():
    color = request.values.get('color')

    if color == 'Red':
        GPIO.output(RED_PIN, GPIO.HIGH)
    elif color == 'Yellow':
        GPIO.output(YELLOW_PIN, GPIO.HIGH)

    return 'ok'


@app.route('/led_off/:color', methods=['POST'])
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
