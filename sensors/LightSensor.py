from sensors.GroveSensor import GroveSensor


class LightSensor(GroveSensor):
    def __init__(self):
        super(LightSensor, self).__init__(channel=6)
