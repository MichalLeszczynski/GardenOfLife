#!/usr/bin/env python
import upm.pyupm_jhd1313m1 as upmjhd
from grove.display.base import *
import sys, mraa

class JHD1802(Display):
    def __init__(self, address = 0x3E):
        self._bus = mraa.I2c(0)
        self._addr = address
        self._bus.address(self._addr)
        if self._bus.writeByte(0):
            print("Check if the LCD {} inserted, then try again"
                    .format(self.name))
            sys.exit(1)
        self.jhd = upmjhd.Jhd1313m1(0, address, address)

    @property
    def name(self):
        return "JHD1802"

    def type(self):
        return TYPE_CHAR

    def size(self):
        return 2, 16

    def clear(self):
        self.jhd.clear()

    def draw(self, data, bytes):
        return False

    def home(self):
        self.jhd.home()

    def setCursor(self, row, column):
        self.jhd.setCursor(row, column)

    def write(self, msg):
        self.jhd.write(msg)

    def _cursor_on(self, enable):
        if enable:
            self.jhd.cursorOn()
        else:
            self.jhd.cursorOff()

    def show_from_file(self, sensors):
        info = ""
        for sensor in sensors:
            name = sensor.__class__.__name__
            with open("data/{}.dat".format(name)) as file:
                info += "{}:{}".format(str(name[0][0]), file.readlines()[-1].split(" ")[2] ) 
        print(info)
        self.clear()
        self.write(info)
