from  HC_sr04 import DistanceSensor
import motors
import threading
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)

#distanceSensor = DistanceSensor()

#currentTime = time.time()
#while(time.time() - currentTime < 20):
#    distanceSensor.updateDistanceValue()

#distanceSensor.exit()


class SensorThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.close = False
        self.isClosed = False
        self.distanceSensor = DistanceSensor()

    def run(self):
        while(not self.close):
            self.distanceSensor.updateDistanceValue()
        self.distanceSensor.exit()
        self.isClosed = True

    def end(self):
        self.close = True

    def isRunning(self):
        return not self.isClosed

    def getDistance(self):
        return self.distanceSensor.getDistance()



sensorThread = SensorThread()
sensorThread.start()

print sensorThread.getDistance()

time.sleep(1)

print sensorThread.getDistance()

sensorThread.end()

sensorThread.join()
