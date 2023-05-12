import smbus2
import time

bus = smbus2.SMBus(1)
i2c_address = 0x49

while True:
    rd = bus.read_word_data(i2c_address, 0)
    data = ((rd & 0xFF) << 8) | ((rd & 0xFF00) >> 8)
    data = data >> 2
    print("Data: ", data)
    time.sleep(1)
