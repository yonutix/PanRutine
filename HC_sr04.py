import RPi.GPIO as GPIO
import time



TRIG = 8
ECHO = 10


class DistanceSensor:

    #Trigger high, trigger low, echo low, echo high
    EMIT_START=1
    WAIT=2
    EMIT_END=3
    RECEIVE_START=4
    RECEIVE_END=5

    def __init__(self):
        self.currentState = DistanceSensor.EMIT_START
        self.waitCounter = 0
        self.timelapseCounter = 0
        self.distance = -1
        self.tmpDistance = 0
        self.setupDistanceSensor()
        print("Sensor initialized")

    def setupDistanceSensor(self):
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        GPIO.output(TRIG, False)
        time.sleep(2)


    def updateDistanceValue(self):
        
        if self.currentState == DistanceSensor.EMIT_START:
            GPIO.output(TRIG, True)
            self.currentState = DistanceSensor.WAIT
            self.waitCounter = time.time()
        
        if self.currentState == DistanceSensor.WAIT:
            if time.time() - self.waitCounter >= 0.5:
                GPIO.output(TRIG, False)
                self.timelapseCounter = time.time()
                self.currentState = DistanceSensor.EMIT_END
        
        if self.currentState == DistanceSensor.EMIT_END:
            if (GPIO.input(ECHO) == 1):
                self.currentState = DistanceSensor.RECEIVE_START
        
        if self.currentState == DistanceSensor.RECEIVE_START:
            if GPIO.input(ECHO) == 0:
                self.distance = time.time() - self.timelapseCounter
                self.distance = self.distance * 17150
                #self.distance = round(self.distance, 2)
                self.currentState = DistanceSensor.EMIT_START
                self.waitCounter = time.time()
                print "Distance:",self.distance,"cm"

        if self.currentState == DistanceSensor.RECEIVE_END:
            if time.time() - self.waitCounter >= 1.0:
                self.currentState = DistanceSensor.EMIT_START

    def getDistance(self):
        return self.distance

    def exit(self):
        GPIO.cleanup()


