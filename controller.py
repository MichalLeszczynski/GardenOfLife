from moisture_sensor import GroveMoistureSensor
from light_sensor import GroveLightSensor

moisture_sensor = GroveMoistureSensor(4)
print("Moisture: {}".format(moisture_sensor.moisture))


light_sensor = GroveLightSensor(6)
print("Light: {}".format(light_sensor.light))

import seeed_dht
temp_humi_sensor = seeed_dht.DHT("11",12)
readed = temp_humi_sensor.read()
print("Humidity: {} \nTemperature: {} ".format(readed[0], readed[1]))
