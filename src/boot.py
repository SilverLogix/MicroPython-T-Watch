# ---------- #


from machine import freq
from micropython import alloc_emergency_exception_buf

# noinspection PyArgumentList
freq(240_000000)
alloc_emergency_exception_buf(100)


print(f"\n Booting... \n")
