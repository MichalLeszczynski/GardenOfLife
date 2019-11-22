from moisture_sensor import GroveMoistureSensor
from light_sensor import GroveLightSensor
from GroveSensor import GroveSensor

moisture_sensor = GroveSensor(4)
print("Moisture: {}".format(moisture_sensor.value))


light_sensor = GroveSensor(6)
print("Light: {}".format(light_sensor.value))


import seeed_dht

temp_humi_sensor = seeed_dht.DHT("11", 12)
readed = temp_humi_sensor.read()
print("Humidity: {} \nTemperature: {} ".format(readed[0], readed[1]))
