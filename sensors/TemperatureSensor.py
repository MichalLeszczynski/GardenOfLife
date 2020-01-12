from sensors.TemperatureHumiditySensor import TemperatureHumiditySensor


class TemperatureSensor(TemperatureHumiditySensor):

    @property
    def value(self):
        self.read_values()
        return self.temperature
