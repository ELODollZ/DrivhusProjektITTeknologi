#! /usr/bin/env python3
# Sources:
# https://www.tutorialspoint.com/python3/python_multithreading.htm
# Author: NyboMønster
# Imports fra system
#import machine
import time
import threading
import queue
# Imports fra egne scripts
from NumberGen import NumberGen
from Timer import Timer
# Variables
exitFlag = 0
PumpCondition = True
LysLampsCondition = True
JordFugtCondition = True

# MainCode
class myThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print ("Starting " + self.name)
        print ("Exiting " + self.name)
          
def PumpThread(threadName, CooldownTimerThread, PumpCondition):
    while PumpCondition == True:
        print("Pump True Works")
        time.sleep(1)
        PumpCondition = False
        return PumpCondition
    while PumpCondition == False:
        print("Pump False Works")
        PumpCondition = True
        return PumpCondition
        
def LysThread(threadName, LysLampsCondition):
    while LysLampsCondition == True:
        print("Lys True Works")
        time.sleep(1)
        LysLampsCondition = False
        return LysLampsCondition
    while LysLampsCondition == False:
        print("Lys False Works")
        LysLampsCondition = True
        return LysLampsCondition        
def JordFugtThread(threadName, JordFugtCondition):
    while JordFugtCondition == True:
        print("JordFugt True Works")
        time.sleep(1)
        JordFugtCondition = False
        return JordFugtCondition
    while JordFugtCondition == False:
        print("JordFugt False Works")
        JordFugtCondition = True
        return JordFugtCondition
# Create new Thread
thread1 = PumpThread(PumpThread, 5.0, PumpCondition)
thread2 = LysThread(LysThread, LysLampsCondition)
thread3 = JordFugtThread(JordFugtThread, JordFugtCondition)

# Start new threads
thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
print ("Exiting Main Thread")