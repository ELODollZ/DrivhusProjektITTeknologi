import smbus2
import time


# import required modules
from machine import ADC, Pin
import utime

# use variables instead of numbers:
soil = ADC(Pin(26)) # Soil moisture PIN reference


bus = smbus2.SMBus(1) # RPi revision 2 (0 for revision 1)
i2c_address = 0x49  # default address
#Calibraton values
min_moisture=0
max_moisture=65535

readDelay = 0.5 # delay between readings

while True:
    # read moisture value and convert to percentage into the calibration range
    moisture = (max_moisture-soil.read_u16())*100/(max_moisture-min_moisture) 
    # print values
    print("moisture: " + "%.2f" % moisture +"% (adc: "+str(soil.read_u16())+")")
    utime.sleep(readDelay) # set a delay between readings
    
    