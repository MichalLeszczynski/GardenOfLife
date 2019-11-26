from activators.Activator import Activator
from controllers.GpioPin import GpioPin


class RelayControlled(Activator):
    def __init__(self, pin):
        super().__init__()
        self.power = GpioPin(pin)

    def on(self):
        super().on()
        self.power.on()

    def off(self):
        super().off()
        self.power.off()
