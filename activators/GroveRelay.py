from activators.RelayControlled import RelayControlled


class GroveRelay(RelayControlled):
        def __init__(self):
            super().__init__(pin=18)
