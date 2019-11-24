from activators.RelayControlled import RelayControlled


class Pump(RelayControlled):
    def __init__(self):
        super(Pump, self).__init__(pin=21)
