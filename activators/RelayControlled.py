from activators.Activator import Activator
from controllers.GpioPin import GpioPin


class RelayControlled(Activator):
    def __init__(self, pin):
        self.power = GpioPin(pin)

    def on(self):
        self.power.on()

    def off(self):
        self.power.off()
