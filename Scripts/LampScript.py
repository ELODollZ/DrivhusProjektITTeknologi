#!/usr/bin/env python3
# Author: NyboMønster
# Imports List
from datetime import datetime, timedelta
import RPi.GPIO as GPIO
import time

#Config List:
RedLamps = 9
BlueLamps = 10
BlueDCylce = 70
RedDCylce = 60

# Variable List:
formatForTime = ("%d/%m/%Y %H:%M:%S%f") [:-6]
CurrentTimeAndDate = datetime.utcnow().strftime(f"%d/%m/%Y %H:%M:%S%f") [:-6]
CheckTimer = str(datetime.strptime("12:00:00", "%H:%M:%S"))
#dateTime =
Var1 = 1000
RedPiPwm = GPIO.PWM(RedLamps, Var1)
BluePiPwm = GPIO.PWM(BlueLamps, Var1)

#Initialize
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RedLamps, BlueLamps, GPIO.OUT)
RedPiPwm.start(0)
BluePiPwm.start(0)


#Main Code
def UpdateTime(UpdatedTime):
    UpdatedTime = datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S%f") [:-6]
    #print(f"{str(float(UpdatedTime))} - {str(float(CheckTimer))}")
    return UpdatedTime

def LampSensor(RedNewDutyCylce, BlueNewDutyCycle):
    print(CurrentTimeAndDate)
    print(CheckTimer)
    CurrentTime = UpdateTime(CurrentTimeAndDate)
    #print()
    if (time < (hours=20) and time > (hours=00)):
        RedPiPwm.ChangeDutyCycle(RedNewDutyCylce)
        BluePiPwm.ChangeDutyCycle(BlueNewDutyCylce)
        print("Debug1 Evening")
        time.sleep(1)
    elif (time > (hours=8) and time < (hours=20)):
        RedPiPwm.ChangeDutyCycle(RedNewDutyCycle)
        BluePiPwm.ChangeDutyCycle(BlueNewDutycycle)
        print("Debug2 Midday")
        time.sleep(1)
    elif (time < (hours=00) and time > (hours=8)):
        RedPiPwm.ChangeDutyCycle(RedNewDutyCycle)
        BluePiPwm.ChangeDutyCycle(BlueNewDutyCycle)
        print("Debug3 Early morning")
        time.sleep(1)
    else:
        print("Error in input or value, or sensor not connected properly")
    
LampSensor()
