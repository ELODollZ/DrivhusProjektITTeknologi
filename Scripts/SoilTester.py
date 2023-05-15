from smbus2 import SMBus
from time import sleep
bus = SMBus(1)
#b = bus.read_byte_data(80, 0)
BusAdd = 80

while True:
    b = bus.read_i2c_block_data(BusAdd,0,2)
    print(b)
    sleep(1)
    bus.close()
