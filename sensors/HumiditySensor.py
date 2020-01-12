from sensors.TemperatureHumiditySensor import TemperatureHumiditySensor


class HumiditySensor(TemperatureHumiditySensor):

    @property
    def value(self):
        self.read_values()
        return self.humidity
