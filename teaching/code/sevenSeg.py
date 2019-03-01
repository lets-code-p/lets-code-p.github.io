import RPi.GPIO as GPIO
import time
from display import display

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.cleanup()
display(0)