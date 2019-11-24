from sensors.GroveSensor import GroveSensor


class MoistureSensor(GroveSensor):
    def __init__(self):
        super(MoistureSensor, self).__init__(channel=4)
