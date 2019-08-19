import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4,GPIO.OUT)

print('Buzzer on')
GPIO.output(4,GPIO.HIGH)
time.sleep(0.5)

print('Buzzer off')
GPIO.output(4,GPIO.LOW)
time.sleep(0.5)
