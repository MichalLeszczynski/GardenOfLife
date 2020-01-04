from activators.RelayControlled import RelayControlled


class PumpGND(RelayControlled):
    def __init__(self):
        super().__init__(pin=20)
