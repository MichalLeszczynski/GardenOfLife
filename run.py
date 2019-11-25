from sensors.MoistureSensor import MoistureSensor
from sensors.LightSensor import LightSensor
from sensors.TemperatureHumiditySensor import TemperatureHumiditySensor

from activators.Pump import Pump
from activators.ws281x import ws281x
from activators.Heater import Heater

from controllers.TwoPositionController import TwoPositionController

moisture_sensor = MoistureSensor()
light_sensor = LightSensor()
temperature_sensor = TemperatureHumiditySensor()

sensors = [moisture_sensor, light_sensor, temperature_sensor]


pump = Pump()
led = ws281x()
heater = Heater()

activators = [pump, led, heater]


moisture_controller = TwoPositionController(moisture_sensor, pump, 200, 40)
light_controller = TwoPositionController(light_sensor, led, 600, 50)
temperature_controller = TwoPositionController(temperature_sensor, heater, 24, 2)

controllers = [moisture_controller, light_controller, temperature_controller]

if __name__ == "__main__":
    try:
        while True:
            for controller in controllers:
                controller.update()

    except KeyboardInterrupt:
        for activator in activators:
            activator.off()
