import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPIO ports for the 7seg pins
segments = (24,21,5,17,4,25,6,22)
#7seg_segment_pins = (11,7,4,2,1,10,5,3) + resistors inline

for segment in segments:
        GPIO.setup(segment, GPIO.OUT)
        GPIO.output(segment, 1)

# GPIO ports for choosing the digits
digits = (23,12,16,19)
#7seg_digit_pins = (12,9,8,6)

for digit in digits:
        GPIO.setup(digit, GPIO.OUT)
        GPIO.output(digit, 0)

num = {
       '0':(0,0,0,0,0,0,1),
       '1':(1,0,0,1,1,1,1),
       '2':(0,0,1,0,0,1,0),
       '3':(0,0,0,0,1,1,0),
       '4':(1,0,0,1,1,0,0),
       '5':(0,1,0,0,1,0,0),
       '6':(0,1,0,0,0,0,0),
       '7':(0,0,0,1,1,1,1),
       '8':(0,0,0,0,0,0,0),
       '9':(0,0,0,0,1,0,0)
       }


display = '1234'
blinkRate = 1

GPIO.output(23,1) # do not set dots

while True:
        for digit in range(4):
                for loop in range(7):
                        GPIO.output(segments[loop], num[display[digit]][loop])
                GPIO.output(digits[digit], 1)
                time.sleep(blinkRate)
                GPIO.output(digits[digit], 0)
