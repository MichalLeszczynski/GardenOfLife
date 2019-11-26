from run import *
import time

print("Initialized")

while True:
    light_controller.update()
    time.sleep(0.2)
