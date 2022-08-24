import board
import neopixel
import time

on = True

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
while True:

    red = 0 
    blue = 255
    green = 0
    
    if( on ):
        pixels[0] = (red, green, blue)
        pixels.show()
    else:
        pixels[0] = (0, 0, 0)
        pixels.show()

    on = not on
    time.sleep(0.5)
