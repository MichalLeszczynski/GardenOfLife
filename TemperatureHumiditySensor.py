import seeed_dht


class TemperatureHumiditySensor:
    def __init__(self):
        self.sensor = seeed_dht.DHT("11", 12)
        self.read = [0, 0]

    def read(self):
        self.read = self.sensor.read()

    def __repr__(self):
        return "Humidity: {} \nTemperature: {} ".format(self.read[0], self.read[1])

    @property
    def temperature(self):
        return self.read[0]

    @property
    def humidity(self):
        return self.read[1]
