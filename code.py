# License : GPLv2.0
# copyright (c) 2023  Dave Bailey
# Author: Dave Bailey (dbisu, @daveisu)
# Pico and Pico W board support

import board
import neopixel
from duckyinpython import *

pixel = neopixel.NeoPixel(board.GP16, 1)
pixel[0] = (0, 128, 255)
pixel.write()

async def main_loop():
    global button1
    
    button_task = asyncio.create_task(monitor_buttons())
    await asyncio.gather(button_task)
           
asyncio.run(main_loop())