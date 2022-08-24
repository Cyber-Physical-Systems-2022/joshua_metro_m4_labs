import board
import neopixel
import time

def show( pixels, red, green, blue ):
    print( f" RGB = ({red}, {green}, {blue})" )
    pixels[0] = (red, green, blue)
    pixels.show()

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
while True:

    red = 0
    blue = 0
    green = 0
    
    for red in range(255):
        show( pixels, red, green, blue )
    for red in range(255, -1, -1):
        show( pixels, red, green, blue )
    
    for green in range(255):
        show( pixels, red, green, blue )
    for green in range(255, -1, -1):
        show( pixels, red, green, blue )
    
    for blue in range(255):
        show( pixels, red, green, blue )
    for blue in range(255, -1, -1):
        show( pixels, red, green, blue )
