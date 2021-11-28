from sensors.GroveADCSensor import GroveADCSensor


class MoistureSensor(GroveADCSensor):
    def __init__(self):
        super(MoistureSensor, self).__init__(channel=4)
