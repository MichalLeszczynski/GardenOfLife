from GroveSensor import GroveSensor
from TemperatureHumiditySensor import TemperatureHumiditySensor as THSensor
from ws281x import ws281x

moisture_sensor = GroveSensor(4)
print("Moisture: {}".format(moisture_sensor.value))

light_sensor = GroveSensor(6)
print("Light: {}".format(light_sensor.value))

temp_humi_sensor = THSensor()
temp_humi_sensor.read()
print("Temperature: {}".format(temp_humi_sensor.temperature))
print("Humidity: {}".format(temp_humi_sensor.humidity))

led = ws281x()
led.on()
led.off()
