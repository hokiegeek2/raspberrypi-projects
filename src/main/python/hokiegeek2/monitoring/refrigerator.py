import time, logging
from datetime import datetime
import RPi.GPIO as io

class RefrigeratorAccessMonitor:
    '''
    Sets the instance-scoped door, doorOpen, doorPin, and hasBeenOpened attributes
    '''   
    def __init__(self):
        self.hasBeenOpened = False
        self.door=0
        self.doorPin = 20
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

    def _getInput(self):
        io.setmode(io.BCM)
        io.setup(self.doorPin, io.IN, pull_up_down=io.PUD_UP)
        return io

    def startMonitor(self):
        logging.info("Started Monitoring Refrigerator at %s" % datetime.now().strftime("%Y%m%d %H:%M:%S"))
        
        # Get an initialized door sensor
        doorSensor = self._getInput()

        # Start a loop monitoring door open and door close events
        while True:
            # If doorSensor.input(self.doorPin) returns true, this means the door is open 
            if doorSensor.input(self.doorPin):
                if self.hasBeenOpened == False:
                    self.hasBeenOpened = True
                logging.info("Refrigerator opened at %s" % datetime.now().strftime("%Y%m%d %H:%M:%S"))
                # while loop that executes until the door is closed, checking every second
                while doorSensor.input(self.doorPin):
                   time.sleep(1)
                self.door = 0

            if doorSensor.input(self.doorPin) == False:
                if self.door == 0 and self.hasBeenOpened == True:
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
