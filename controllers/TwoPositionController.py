class TwoPositionController:
    def __init__(self, sensor, activator, wanted, hysteresis):
        self.sensor = sensor
        self.activator = activator
        self.wanted = wanted
        self.hysteresis = hysteresis

    def update(self):
        current = self.sensor.value
        if current > self.wanted + self.hysteresis:
            self.activator.off()
        elif current < self.wanted - self.hysteresis:
            self.activator.on()

