#!/usr/bin/env python3
# Sources:
# Author: NyboMønster
# Imports fra system 
#import machine
import time
import random

# Variables:
TestVar1 = ("CameraModule", "PumpModule", "LampSensor", "JordFugtSensor", "SwitchPause")


# Main code
def SwitchFunc(Input):
    match Input:
        case "CameraModule":
            print("CamWorks Works")
        case "PumpModule":
            print("PumpWater Works")
        case "LampSensor":
            print("LampSensor Works")
        case "JordFugtSensor":
            print("Test Jordfugtsensor")
        case "SwitchPause":
            print("Paused SwitchCase")
        case _:
            print("Sleeper time")
# Main Loop
while True:
    ranPick = random.choice(TestVar1)
    SwitchFunc(ranPick)
    time.sleep(1)
