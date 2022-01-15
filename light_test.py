from nanoleafapi import nanoleaf
import time
import lights

#demonstration of the lightwall animation.
lights.allOn(nanoleaf.GREEN)
lights.allSetBright(100)

#what would happen as you move away from the sensor
lights.n1.set_brightness(0)
time.sleep(1)
lights.n2.set_brightness(0)
lights.n3.set_brightness(0)
time.sleep(1)
lights.n4.set_brightness(0)
lights.n5.set_brightness(0)
time.sleep(1)
lights.n6.set_brightness(0)
lights.n7.set_brightness(0)
time.sleep(1)
lights.n8.set_brightness(0)
lights.n9.set_brightness(0)
time.sleep(1)
lights.n10.set_brightness(0)

#as you move closer to the sensor
lights.n1.set_brightness(100)
time.sleep(1)
lights.n2.set_brightness(100)
lights.n3.set_brightness(100)
time.sleep(1)
lights.n4.set_brightness(100)
lights.n5.set_brightness(100)
time.sleep(1)
lights.n6.set_brightness(100)
lights.n7.set_brightness(100)
time.sleep(1)
lights.n8.set_brightness(100)
lights.n9.set_brightness(100)
time.sleep(1)
lights.n10.set_brightness(100)