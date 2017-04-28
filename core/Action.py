# import RPi.GPIO as GPIO
import logging
from utils.Validator import Validate
from time import sleep




class Action:

    def __init__(self):
        self._checker = Validate()
        self.actionType = self._checker.get_actiontype()
        # GPIO.setmode(GPIO.BCM)
        logging.debug("action Ready")

    def exec(self):
        logging.debug("action type : " + self.actionType)
        if self.actionType == "blink":
            self.blink()


    def blink(self):
        timer = self._checker.get_blinkTime()
        pin = self._checker.get_pinId()
        # GPIO.set(pin, GPIO.output)
        logging.debug("on " + str(pin))
        # GPIO.output(pin, GPIO.HIGH)
        sleep(timer)
        # GPIO.output(pin, GPIO.LOW)
        logging.debug("off " + str(pin))
