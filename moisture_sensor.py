#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
# Grove Base Hat for the Raspberry Pi, used to connect grove sensors.
# Copyright (C) 2018  Seeed Technology Co.,Ltd.
'''
This is the code for
    - Grove - Moisture Sensor <https://www.seeedstudio.com/Grove-Moisture-Sensor-p-955.html>`_

'''
import math
import sys
import time
from grove.adc import ADC

__all__ = ["GroveMoistureSensor"]

class GroveMoistureSensor:
    '''
    Grove Moisture Sensor class

    Args:
        pin(int): number of analog pin/channel the sensor connected.
    '''
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    @property
    def moisture(self):
        '''
        Get the moisture strength value/voltage

        Returns:
            (int): voltage, in mV
        '''
        value = self.adc.read_voltage(self.channel)
        return value



def main():
    import datetime
    pin = 4
    sensor = GroveMoistureSensor(pin)
    while True:
        m = sensor.moisture
        print('Time: {0}, Moisture value: {1}'.format(datetime.datetime.now(), m))
        with open("moisture.dat", "a+") as moisture_log:
            moisture_log.write(str(datetime.datetime.now()) + " " +  str(m) + "\n")
        time.sleep(1)

if __name__ == '__maain__':
    main()
