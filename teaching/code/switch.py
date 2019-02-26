import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PORT_IN = 18
GPIO.setup(PORT_IN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    input_state = GPIO.input(PORT_IN)
    if input_state == 1:
        print('Button Pressed')
        time.sleep(0.2)