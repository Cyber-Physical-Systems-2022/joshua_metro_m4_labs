import asyncio
import time
import board
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import adafruit_mpl3115a2
import neopixel
i2c = board.I2C()
sensor = adafruit_mpl3115a2.MPL3115A2(i2c)

displayio.release_displays()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(128, 32, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White


bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)
# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(118, 24, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=5, y=4)
splash.append(inner_sprite)

# Draw a label
text_area = label.Label(terminalio.FONT, text="Hello, World!", color=0xFFFF00, x=28, y=15)
splash.append(text_area)

pressure = None
altitude = None
global temperature
temperature = None

async def get_display_temperature():
    global temperature
    while True:
#        pressure = sensor.pressure
#        altitude = sensor.altitude
        temperature = sensor.temperature

        #text = f"Temp: {temperature:0.3f}°C"
        text = f"{temperature:0.3f} deg C"
#        text = f"{pressure:0.3f} P"
        text_area._reset_text(text)

        print(text)
        await asyncio.sleep(0.5)

# The NeoPixel should be blinking blue if the temperature is below 15C and orange if the temperature is above 25C. It should blink twice per second. The light should be green if the temperature is between 15C and 25C.
async def handle_neopixel():

    global temperature

    on = True
    pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
    while True:

        red = 255
        blue = 255
        green = 255

        if( temperature < 15 ):
            red = 0
            blue = 255
            green = 0
        elif( temperature < 25 ):
            red = 0
            blue = 0
            green = 255
        else:
            red = 255
            blue = 0
            green = 50
        
        if( on ):
            pixels[0] = (red, green, blue)
            pixels.show()
        else:
            pixels[0] = (0, 0, 0)
            pixels.show()

        on = not on
        print(f"LED: {on}")
        await asyncio.sleep(0.3)

print("Hello, World!")

async def main():

    temperature_task = asyncio.create_task(get_display_temperature())
    led_task = asyncio.create_task(handle_neopixel())
    await asyncio.gather( temperature_task, led_task )

asyncio.run(main())
