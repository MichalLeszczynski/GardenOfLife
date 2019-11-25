import multiprocessing as mp
import time

from sensors.MoistureSensor import MoistureSensor
from sensors.LightSensor import LightSensor
from sensors.TemperatureHumiditySensor import TemperatureHumiditySensor

from activators.Pump import Pump
from activators.ws281x import ws281x
from activators.Heater import Heater

from controllers.TwoPositionController import TwoPositionController


def run(controller):
    while True:
        controller.update()
        time.sleep(0.5)


moisture_sensor = MoistureSensor()
light_sensor = LightSensor()
temperature_humidity_sensor = TemperatureHumiditySensor()

sensors = [moisture_sensor, light_sensor, temperature_humidity_sensor]


pump = Pump()
led = ws281x()
heater = Heater()

activators = [pump, led, heater]

logging = True

moisture_controller = TwoPositionController(
    moisture_sensor, pump, wanted=200, hysteresis=40, logging=logging
)
light_controller = TwoPositionController(
    light_sensor, led, wanted=600, hysteresis=50, logging=logging
)
temperature_controller = TwoPositionController(
    temperature_humidity_sensor, heater, wanted=24, hysteresis=2, logging=logging
)

controllers = [moisture_controller, light_controller, temperature_controller]

if __name__ == "__main__":
    try:

        pool = mp.Pool(4)
        pool.map(run, controllers)

    except KeyboardInterrupt:
        for activator in activators:
            activator.off()
