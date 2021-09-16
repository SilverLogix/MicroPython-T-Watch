from c_network import *

import debug
import machine
import gc
import random
import utime
import _thread as thread
import gfx
from gfx import *

# --------- Variables --------- #


# -------- Init main code ---------- #

# gfx.micrologo()

# STA('SSID', 'PASS')
# AP("ESP32-AP", 2, True)

# noinspection PyArgumentList
machine.freq(80000000)  # set the CPU frequency to 80 MHz

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


tft.fill(gfx.BLACK)
alarm_0 = 0


def draw():
    while True:
        global alarm_0
        # gfx.triangle(43, 30, 40, 90, 80, 120, st.color565(200,200,200))

        ddd = debug.showVoltage()
        rrr = debug.raw_temp()
        fff = debug.m_freq()

        A = alarm_0 + 1

        gfx.text_long("Sensor", ddd, rrr, "", fff, "", "", A, gfx.WHITE, gfx.BLACK)
        utime.sleep_ms(1000)


# --------- Main Code ---------- #

# thread.start_new_thread(scr_test, ())
thread.start_new_thread(draw, ())
