import RPi.GPIO as GPIO
import time

def display(x):
    a = 19
    b = 6
    c = 13
    d = 26
    e = 25
    f = 16
    g = 20
    h = 21

    '''         a,b,c,d,e,f,g,h  '''
    num = {0  :[1,1,1,1,1,1,1,1],
           1  :[0,0,0,0,0,0,0,0],
           2  :[0,0,0,0,0,0,0,0],
           3  :[0,0,0,0,0,0,0,0],
           4  :[0,0,0,0,0,0,0,0],
           5  :[0,0,0,0,0,0,0,0],
           6  :[0,0,0,0,0,0,0,0],
           7  :[0,0,0,0,0,0,0,0],
           8  :[0,0,0,0,0,0,0,0],
           9  :[0,0,0,0,0,0,0,0]}

    GPIO.setup(a,GPIO.OUT)
    GPIO.setup(b,GPIO.OUT)
    GPIO.setup(c,GPIO.OUT)
    GPIO.setup(d,GPIO.OUT)
    GPIO.setup(e,GPIO.OUT)
    GPIO.setup(f,GPIO.OUT)
    GPIO.setup(g,GPIO.OUT)
    GPIO.setup(h,GPIO.OUT)

    GPIO.output(a, not num[x][0])
    GPIO.output(b, not num[x][1])
    GPIO.output(c, not num[x][2])
    GPIO.output(d, not num[x][3])
    GPIO.output(e, not num[x][4])
    GPIO.output(f, not num[x][5])
    GPIO.output(g, not num[x][6])
    GPIO.output(h, not num[x][7])


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()
display(0)

