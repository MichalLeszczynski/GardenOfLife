from activators.RelayControlled import RelayControlled


class Pump(RelayControlled):
    def __init__(self):
        super().__init__(pin=21)
