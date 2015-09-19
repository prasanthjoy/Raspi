#First code from GitHub
import RPi.GPIO as GPIO
import time

#Comment added to test branching
GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

#Initialize variables
sleep_interval=0.2
led_yellow=11
led_blue=13
led_green=15
led_red=21

def _lightup(pinno):
        GPIO.output(pinno,1)
        time.sleep(sleep_interval)
        GPIO.output(pinno,0)
        return

try:
        while 1:
                _lightup(led_yellow)
                _lightup(led_blue)
                _lightup(led_green)
                _lightup(led_red)
except KeyboardInterrupt:
        print "GPIO Stopped"
        GPIO.cleanup()
        print "GPIO Cleaned Up"
        print "Copyright C Prasanth Joy 2015"

