import RPi.GPIO as GPIO
from utils import config
from flask import Flask, request
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)






@app.route("/")