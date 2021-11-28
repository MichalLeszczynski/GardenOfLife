import asyncio

from sensors.UltrasonicRangeSensor import UltrasonicRangeSensor

from activators.GroveRelay import GroveRelay

from controllers.TwoPositionController import TwoPositionController



async def run(controller):
    print("Starting controller containing: {} and {}".format(controller.sensor.__class__.__name__, controller.activator.__class__.__name__))
    while True:
        controller.update()
        await asyncio.sleep(0.5)


range_sensor = UltrasonicRangeSensor()

sensors = [range_sensor]


relay = GroveRelay()


activators = [relay]

logging = True

fun_controller = TwoPositionController(
    range_sensor, relay, wanted=100, hysteresis=0, logging=logging
)


controllers = [fun_controller]


def main():
    try:
        relay.on()
        loop = asyncio.get_event_loop()

        for controller in controllers:
            loop.create_task(run(controller))
        loop.run_forever()

    except KeyboardInterrupt:
        for activator in activators:
            activator.off()
        relay.off()


if __name__ == "__main__":
    main()
