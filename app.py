import RPi.GPIO as GPIO
from flask import Flask, render_template


RED_PIN = 14
YELLOW_PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)


app = Flask(__name__)


@app.route('/led_on', methods=['POST'])
def led_on():
    GPIO.output(RED_PIN, GPIO.HIGH)
    return 'ok'


@app.route('/led_off', methods=['POST'])
def led_off():
    GPIO.output(RED_PIN, GPIO.LOW)
    return 'ok'


@app.route('/', methods=['GET'])
def home():
    return render_template('button.html', title='Button', name='Isaac Krementsov')
