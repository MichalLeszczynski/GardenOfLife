from datetime import datetime


class TwoPositionController:
    def __init__(self, sensor, activator, wanted, hysteresis, logging=False, dry=False):
        self.sensor = sensor
        self.activator = activator
        self.wanted = wanted
        self.hysteresis = hysteresis
        self.logging = logging
        self.dry = dry

    def update(self):
        current = self.sensor.value

        if self.logging:
            with open("data/{}.dat".format(self.sensor.__class__.__name__), "a+") as data:
                time = datetime.now()
                record = "{} {} {} {}\n".format(
                    time, current, self.wanted, self.hysteresis
                )
                data.write(record)

        if not self.dry:
            if current > self.wanted + self.hysteresis and self.activator.is_on:
                self.activator.off()
            elif current < self.wanted - self.hysteresis and not self.activator.is_on:
                self.activator.on()
