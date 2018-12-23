#!/usr/bin/env python3
from itertools import cycle

# Open up the encrypted image as bytes
with open("cat_final", "rb") as f:
    file = f.read()

# The first eight bytes of a PNG file always contain the following (decimal) values:
header = bytes([137, 80, 78, 71, 13, 10, 26, 10])

# Fix IHDR
header += bytes([0, 0, 0, 0x0d])
header += b'IHDR'

# fix header and create file
file = header + file[len(header):]
with open("cat_fixed.png", "wb") as f:
    f.write(file)
