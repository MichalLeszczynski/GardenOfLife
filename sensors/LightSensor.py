from sensors.GroveADCSensor import GroveADCSensor


class LightSensor(GroveADCSensor):
    def __init__(self):
        super(LightSensor, self).__init__(channel=6)
