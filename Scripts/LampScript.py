#!/usr/bin/env python3
# Author: NyboMønster
# Imports List
from datetime import datetime, timedelta, date
#import RPi.GPIO as GPIO
import time

#Config List:
RedLamps = 9
BlueLamps = 10
BlueDCylce = 70
RedDCylce = 60

# Variable List:
formatForDateAndTime = ("%d/%m/%Y %H:%M:%S%f") [:-6]
dateTime = time.struct_time(tm_year=2022, tm_mon=3, tm_mday=1, tm_hour=14, tm_min=51, tm_sec=19, tm_wday=4, tm_yday=60, tm_isdst=0)
CurrentTimeAndDate = datetime.utcnow().strftime(f"%d/%m/%Y %H:%M:%S%f") [:-6]
Var1 = 1000
#RedPiPwm = GPIO.PWM(RedLamps, Var1)
#BluePiPwm = GPIO.PWM(BlueLamps, Var1)
RedPiPwm = 0
bluePiPwm = 0
#Initialize
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(RedLamps, BlueLamps, GPIO.OUT)
#RedPiPwm.start(0)
#BluePiPwm.start(0)


#Main Code
def UpdateTime(UpdatedTime):
    UpdatedTime = datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S%f") [:-6]
    print(Time)
    return UpdatedTime

def LampSensor(RedNewDutyCylce, BlueNewDutyCycle):
    print(CurrentTimeAndDate)
    CurrentTime = UpdateTime(CurrentTimeAndDate)
    print(CurrentTime)
    print(dateTime)
    print("Debug 0, Timer Check")
    if (CurrentTime < (hours==20) and CurrentTime > (hours==00)):
        RedPiPwm.ChangeDutyCycle(RedNewDutyCylce)
        BluePiPwm.ChangeDutyCycle(BlueNewDutyCylce)
        print("Debug1 Evening")
        time.sleep(1)
    elif (CurrentTime > (hours==8) and CurrentTime < (hours==20)):
        RedPiPwm.ChangeDutyCycle(RedNewDutyCycle)
        BluePiPwm.ChangeDutyCycle(BlueNewDutycycle)
        print("Debug2 Midday")
        time.sleep(1)
    elif (CurrentTime < (hours==00) and CurrentTime > (hours==8)):
        RedPiPwm.ChangeDutyCycle(RedNewDutyCycle)
        BluePiPwm.ChangeDutyCycle(BlueNewDutyCycle)
        print("Debug3 Early morning")
        time.sleep(1)
    else:
        print("Error in input or value, or sensor not connected properly") 
LampSensor(40, 50)
