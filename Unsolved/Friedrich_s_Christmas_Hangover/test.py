#!/usr/bin/env python3
from itertools import cycle

# Open up file as bytes
with open("chall", "rb") as f:
    file = f.read()

# Fix the header
header = bytes([0x7f, 0x45, 0x4c, 0x46])

# fix header and create file
file = header + file[len(header):]
with open("chall_fixed", "wb") as f:
    f.write(file)
