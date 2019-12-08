from activators.RelayControlled import RelayControlled


class RelayPower(RelayControlled):
    def __init__(self):
        super().__init__(pin=26)
