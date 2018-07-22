import time, logging
from datetime import datetime
import RPi.GPIO as io

class RefrigeratorAccessMonitor:
    '''
    Sets the instance-scoped door, doorOpen, doorOpened, and doorPin attributes
    '''   
    def __init__(self):
        self.doorOpened = 0
        self.doorOpen = False
        self.door=0
        self.doorPin = 20
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

    def _getInput(self):
        io.setmode(io.BCM)
        io.setup(self.doorPin, io.IN, pull_up_down=io.PUD_UP)
        return io

    def startMonitor(self):
        logging.info("Started Monitoring Refrigerator at %s" % datetime.now().strftime("%Y%m%d %H:%M:%S"))

        doorSensor = self._getInput()
        while True:
            '''
            If doorSensor.input(self.doorPin) returns true, this means the door is open 
            '''
            if doorSensor.input(self.doorPin):
                self.doorOpened += 1
                logging.info("Refrigerator opened at %s" % datetime.now().strftime("%Y%m%d %H:%M:%S"))
                while doorSensor.input(self.doorPin):
                   time.sleep(1)
                self.door = 0

            if doorSensor.input(self.doorPin) == False:
                if (self.door == 0):
                    logging.info("Refrigerator closed at %s" % datetime.now().strftime("%Y%m%d %H:%M:%S"))
                    self.door += 1

'''
Starts the refrigerator monitoring daemon
'''
def main():    
    monitor = RefrigeratorAccessMonitor()
    monitor.startMonitor()
    
if  __name__ =='__main__':
    main()
