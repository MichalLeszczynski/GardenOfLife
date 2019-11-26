from datetime import datetime
from other.decorators import slow_down

class TwoPositionController:
    def __init__(self, sensor, activator, wanted, hysteresis, logging=False):
        self.sensor = sensor
        self.activator = activator
        self.wanted = wanted
        self.hysteresis = hysteresis
        self.logging = logging

    @slow_down(slow_amount=0.5)
    def update(self):
        current = self.sensor.value

        if self.logging:
            with open("{}.dat".format(self.sensor.__class__.__name__), "a+") as data:
                time = datetime.now()
                record = "{} {} {} {}\n".format(
                    time, current, self.wanted, self.hysteresis
                )
                data.write(record)

        if current > self.wanted + self.hysteresis and self.activator.is_on:
            print("Setting {} OFF".format(self.activator.__class__.__name__))
            self.activator.off()
        elif current < self.wanted - self.hysteresis and not self.activator.is_on:
            print("Setting {} ON".format(self.activator.__class__.__name__))
            self.activator.on()
