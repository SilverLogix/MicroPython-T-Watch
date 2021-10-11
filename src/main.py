

from debug import b_print
from machine import Pin
from machine import SPI
from machine import freq

import gc
import random
import utime
import _thread as thread
import st7789 as st

# ----------- Variables ------------ #

#

# -------- Init main code ---------- #

tft = st.ST7789(
    SPI(1, baudrate=30000000, sck=Pin(18), mosi=Pin(19)),
    135, 240,
    reset=Pin(23, Pin.OUT),
    cs=Pin(5, Pin.OUT),
    dc=Pin(16, Pin.OUT),
    backlight=Pin(4, Pin.OUT),
    rotation=3)

tft.init()

b_print()
tft.fill(tft.BLACK)

# noinspection PyArgumentList
freq(160_000000)  # set the CPU frequency to 80 MHz

gc.collect()


# ---------- Create Objects --------- #

def scr_test():
    try:
        for rotation in range(4):
            tft.rotation(rotation)
            tft.fill(0)
            col_max = tft.width() - tft.font.WIDTH * 6
            row_max = tft.height() - tft.font.HEIGHT

            for _ in range(128):
                utime.sleep_ms(100)
                tft.text(tft.font, "Hello!",
                         random.randint(0, col_max),
                         random.randint(0, row_max),
                         tft.color565(
                             random.getrandbits(8),
                             random.getrandbits(8),
                             random.getrandbits(8)),
                         tft.color565(
                             random.getrandbits(8),
                             random.getrandbits(8),
                             random.getrandbits(8))
                         )
    except KeyboardInterrupt:
        thread.exit()


# --------- Main Code ---------- #

thread.start_new_thread(scr_test, ())
