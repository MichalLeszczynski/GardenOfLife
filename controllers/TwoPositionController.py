from datetime import datetime


class TwoPositionController:
    def __init__(self, sensor, activator, wanted, hysteresis, logging=False):
        self.sensor = sensor
        self.activator = activator
        self.wanted = wanted
        self.hysteresis = hysteresis
        self.logging = logging

    def update(self):
        current = self.sensor.value

        if self.logging:
            with open("{}.dat".format(self.sensor.__class__), "a+") as data:
                time = datetime.now()
                record = "{} {} {} {}".format(
                    time, current, self.wanted, self.hysteresis
                )
                data.write(record)

        if current > self.wanted + self.hysteresis:
            self.activator.off()
        elif current < self.wanted - self.hysteresis:
            self.activator.on()
