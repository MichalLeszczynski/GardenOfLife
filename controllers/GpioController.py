import os
import time
from other import decorators


class GpioController:
    def __init__(self):
        self.gpio_path = "/sys/class/gpio/"
        self.export_path = self.gpio_path + "export"

    def on(self, pin):
        self.initialize_pin(pin)
        self.set_value(pin, 1)

    def off(self, pin):
        self.initialize_pin(pin)
        self.set_value(pin, 0)

    def initialize_pin(self, pin):
        if not self.is_exported(pin):
            with open(self.export_path, "w") as export:
                export.write(str(pin))

        if not self.is_set_to_out(pin):
            with open(self.direction(pin), "w") as direction:
                direction.write("out")

    def set_value(self, pin, val):
        with open(self.pin_dir(pin) + "/value", "w") as value:
            value.write(str(val))

    def is_exported(self, pin):
        return os.path.exists(self.pin_dir(pin))

    def is_set_to_out(self, pin):
        with open(self.pin_dir(pin) + "/direction", "r") as direction:
            return direction.read() is "out"

    def pin_dir(self, pin):
        return self.gpio_path + "gpio" + str(pin)

    def direction(self, pin):
        return self.pin_dir(pin) + "/direction"


if __name__ == "__main__":

    @decorators.timer
    @decorators.debug
    def pin_test(pin):
        controller = GpioController()
        for _ in range(20):
            controller.on(pin)
            time.sleep(0.2)
            controller.off(pin)
            time.sleep(0.2)

    pin = 25
    pin_test(pin)
