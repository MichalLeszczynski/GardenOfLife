from sensors.Sensor import Sensor
from grove.adc import ADC


class GroveADCSensor(Sensor):
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    @property
    def value(self):
        val = self.adc.read_voltage(self.channel)
        return val
