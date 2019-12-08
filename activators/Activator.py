class Activator:
    def __init__(self):
        self.is_on = False

    def on(self):
        print("Setting {} ON".format(self.__class__.__name__))
        self.is_on = True

    def off(self):
        print("Setting {} OFF".format(self.__class__.__name__))
        self.is_on = False
