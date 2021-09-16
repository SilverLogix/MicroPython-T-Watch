import micropython
import gc
import machine
import debug
import gfx
import utime
import axp202c as axp202


# import webrepl

# DO NOT GO BELOW 80Mhz!!!  Will break wifi and complicate serial!
machine.freq(240000000)
utime.sleep_ms(100)

micropython.alloc_emergency_exception_buf(100)
print('Booting...')
axp = axp202.PMU()
axp.enablePower(axp202.AXP202_LDO2)
axp.enablePower(axp202.AXP202_DCDC3)
axp.clearIRQ()

gfx.boot()

# webrepl.start(password="password")

debug.space_free()
debug.m_freq()
debug.raw_temp()
debug.showVoltage()

gc.collect()
