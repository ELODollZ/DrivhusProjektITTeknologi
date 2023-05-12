import smbus2
import time

class MCP3021:
    bus = smbus2.SMBus(1)

    def __init__(self, address = 0x49):
        self.address = address
    def readRaw(self):
        rd = self.bus.read_word_data(self.address, 0)
        data = ((rd & 0xFF) << 8) | ((rd & 0xFF00) >> 8)
        return data >> 2

adc = MCP3021()

while True:
    raw = adc.readRaw()
    print("RawOutput :", raw)
    time.sleep(1)
