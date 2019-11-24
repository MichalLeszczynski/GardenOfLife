from activators.RelayControlled import RelayControlled


class Heater(RelayControlled):
    def __init__(self):
        super(Heater, self).__init__(pin=26)
