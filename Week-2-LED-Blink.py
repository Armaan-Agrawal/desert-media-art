print('Hello Desert art World - 2022!')
print("Let's Blink!!")

import board
import digitalio # gives us access to the pin
import time

#print("The Basic LED is attached to pin " + board.LED)

# This variable gives access to the hardware pin
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

starttime = time.monotonic()
secondsToBlink = 5
print("It is now " + str(starttime))
print("Starting to Blink")
while (time.monotonic() - starttime < secondsToBlink):
    led.value = True
    time.sleep(0.5/2)
    led.value = False
    time.sleep(0.5/2)
    print("\ttime - %.1f" % time.monotonic())

print("All Done")
