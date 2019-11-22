from controllers.GpioController import GpioController


class GpioPin:
    def __init__(self, pin):
        self.controller = GpioController()
        self.pin = pin

    def on(self):
        self.controller.on(self.pin)

    def off(self):
        self.controller.off(self.pin)
