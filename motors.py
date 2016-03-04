import RPi.GPIO as GPIO
import time
 

class Motors:
    Motor1A = 16
    Motor1B = 18
    Motor2A = 22
    Motor2B = 40
    
    LEFT_WHEEL = 1
    RIGHT_WHEEL = 2

    FORWARD = 1
    BACKWARD = 2
    def __init__(self):
        GPIO.setup(Motors.Motor1A,GPIO.OUT)
        GPIO.setup(Motors.Motor1B,GPIO.OUT)
    
        GPIO.setup(Motors.Motor2A,GPIO.OUT)
        GPIO.setup(Motors.Motor2B,GPIO.OUT)

        GPIO.output(Motors.Motor1A,GPIO.LOW)
        GPIO.output(Motors.Motor2A,GPIO.LOW)
        GPIO.output(Motors.Motor1B,GPIO.LOW)
        GPIO.output(Motors.Motor2B,GPIO.LOW)

    def go(self, wheel, direction, duration):
        if (wheel == Motors.LEFT_WHEEL):
            if (direction == Motors.FORWARD):
                print 1
                GPIO.output(Motors.Motor1A,GPIO.HIGH)
                GPIO.output(Motors.Motor1B,GPIO.LOW)
                time.sleep(duration)
                GPIO.output(Motors.Motor1A,GPIO.LOW)
            if(direction == Motors.BACKWARD):
                print 2
                GPIO.output(Motors.Motor1A,GPIO.LOW)
                GPIO.output(Motors.Motor1B,GPIO.HIGH)
                time.sleep(duration)
                GPIO.output(Motors.Motor1B,GPIO.LOW)
        if (wheel == Motors.RIGHT_WHEEL):
            if (direction == Motors.FORWARD):
                print 3
                GPIO.output(Motors.Motor2A,GPIO.HIGH)
                GPIO.output(Motors.Motor2B,GPIO.LOW)
                time.sleep(duration)
                GPIO.output(Motors.Motor2A,GPIO.LOW)
            if(direction == Motors.BACKWARD):
                print 4
                GPIO.output(Motors.Motor2A,GPIO.LOW)
                GPIO.output(Motors.Motor2B,GPIO.HIGH)
                time.sleep(duration)
                GPIO.output(Motors.Motor2B,GPIO.LOW)
    def exit(self):
        GPIO.cleanup()




