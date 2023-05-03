#! /usr/bin/env python3
# Author: NyboMønster
# Imports fra system
import random
# from time import sleep
# Variables

# MainCode
def NumberGen():
    Pump = random.randint(0, 1)
    if Pump == 0:
        Pump = bool(Pump)
    elif Pump == 1:
        Pump = bool(Pump)
    else:
        print("Error in code somewhere, or no Inputs")
    LysLamps= random.randint(1, 100)
    JordFugt = random.randint(1, 5000)
    print(JordFugt, LysLamps, Pump)
    return JordFugt, LysLamps, Pump
    # sleep(0.5)
# NumberGen()
