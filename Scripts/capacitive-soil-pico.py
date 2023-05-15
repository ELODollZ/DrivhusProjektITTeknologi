import smbus2
import time


# import required modules
#from machine import ADC, Pin
#import utime

# use variables instead of numbers


bus = smbus2.SMBus(1) # RPi revision 2 (0 for revision 1)
i2c_address = 0x49  # default address
#Calibraton values
min_moisture=0
max_moisture=65535

#readDelay = 0.5 # delay between readings

while True:
    # read moisture value and convert to percentage into the calibration range
   # moisture = (max_moisture-soil.read_u16())*100/(max_moisture-min_moisture) 
    # print values
    #print("moisture: " + "%.2f" % moisture +"% (adc: "+str(soil.read_u16())+")")
    #utime.sleep(readDelay) # set a delay between readings
    adcval=bus.read_i2c_block_data(i2c_address, 0, 2)
    print(adcval)
    time.sleep(0.5)
