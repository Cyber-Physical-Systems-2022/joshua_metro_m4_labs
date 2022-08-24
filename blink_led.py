import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

interval = 1

while True:
    led.value = True
    time.sleep(interval)
    led.value = False
    time.sleep(interval)

    interval -= 0.1

    if(interval <= 0):
        interval = 1 
