import asyncio

from sensors.MoistureSensor import MoistureSensor
from sensors.LightSensor import LightSensor
from sensors.TemperatureSensor import TemperatureSensor
from sensors.HumiditySensor import HumiditySensor

from activators.Pump import Pump
from activators.PumpGND import PumpGND
from activators.ws281x import ws281x
from activators.Heater import Heater
from activators.RelayPower import RelayPower

from controllers.TwoPositionController import TwoPositionController


from other.jhd1802 import JHD1802


async def run(controller):
    print("Starting controller containing: {} and {}".format(controller.sensor.__class__.__name__, controller.activator.__class__.__name__))
    while True:
        controller.update()
        await asyncio.sleep(0.5)


async def show_latest_info(sensors, lcd):
    while True:
        lcd.show_from_file(sensors)
        await asyncio.sleep(0.5)

moisture_sensor = MoistureSensor()
light_sensor = LightSensor()
temperature_sensor = TemperatureSensor()
humidity_sensor = HumiditySensor()

sensors = [moisture_sensor, light_sensor, temperature_sensor, humidity_sensor]


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
    temperature_sensor, heater, wanted=24, hysteresis=2, logging=logging, dry=True
)

humidity_controller = TwoPositionController(
    humidity_sensor, logging=logging, dry=True
)

controllers = [light_controller, moisture_controller, temperature_controller, humidity_controller]

relay = RelayPower()
pump_gnd = PumpGND()

lcd = JHD1802()


def main():
    try:
        relay.on()
        pump_gnd.on()
        loop = asyncio.get_event_loop()

        for controller in controllers:
            loop.create_task(run(controller))
        loop.create_task(show_latest_info(sensors, lcd=lcd))
        loop.run_forever()

    except KeyboardInterrupt:
        for activator in activators:
            activator.off()
        relay.off()
        pump_gnd.off()


if __name__ == "__main__":
    main()
