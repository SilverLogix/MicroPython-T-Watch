
def space_free():  # Display remaining free space
    from os import statvfs

    print('')
    bits = statvfs('/flash')
    print(str(bits))
    blksize = bits[0]  # 4096
    blkfree = bits[3]  # 12
    freesize = blksize * blkfree  # 49152
    mbcalc = 1024 * 1024  # 1048576
    mbfree = freesize / mbcalc  # 0.046875
    print(str(mbfree))
    print('')


def m_freq():
    import machine

    gfr = str(machine.freq())

    # print(gfr)

    fff = gfr
    return fff


def raw_temp():
    import esp32

    raw = str(esp32.raw_temperature())
    rtemp = ("CPU Temp: " + raw + "F")
    # print(rtemp)
    rrr = rtemp
    return rrr



def showVoltage():
    from machine import ADC, Pin

    adc = ADC(Pin(32))

    vref = 1100

    v = adc.read()
    battery_voltage = (float(v) / 4095.0) * 2.0 * 3.3 * (vref / 1000.0)
    # voltage = ("Voltage :" + str(battery_voltage) + "V")
    voltage = ("Voltage: {0:0.2f}v".format(battery_voltage))
    # print(voltage)

    ddd = voltage
    return ddd
