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
        all_info = ""
        line_1 = ""
        line_2 = ""
        i = 0
        for sensor in sensors:
            name = sensor.__class__.__name__
            with open("data/{}.dat".format(name)) as file:
                tmp_info = "{}:{:4d} ".format(str(name[0][0]), int(file.readlines()[-1].split(" ")[2]) )
                all_info += tmp_info
            if i < 2: # go to a new line in display after displaying data from 2 sensors
                line_1 += tmp_info
            else:
                line_2 += tmp_info 
            i += 1
        print(all_info)
        self.clear()
        self.write(line_1)
        self.setCursor(1,0)
        self.write(line_2)
