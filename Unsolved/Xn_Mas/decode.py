#!/usr/bin/env python3
import string
printable = bytes(string.ascii_letters + string.digits + '!"#$%&\'()*+,-./:;?@[\\]^_`{|}~', 'ascii')


modulo = 1705110751
result = 25741138

f0 = 125
f1 = 3458

print("==================================")
print(">> Pos 0")

k0 = 0
pos = 0
for k in range(256):
    f = result + k * modulo

    if (f & 0xFF == f0):
        try:
            hex_str = hex(f)[2:]
            byte_str = bytes.fromhex(hex_str)
            print(f"\rFound pos={pos}, k={hex(k)}, f={hex(f)}:", byte_str)
            k0 = k
        except:
            pass

print("==================================")
print(">> Pos 1")

k1s = []
pos = 1
for k1 in range(256):
    k = k0 + k1 * (0x100)
    f = result + k * modulo

    try:
        hex_str = hex(f)[2:]
        byte_str = bytes.fromhex(hex_str)
        if (byte_str[::-1])[pos] in printable:
            k1s.append(k1)
            print(f"\rFound pos={pos}, k={hex(k)}, f={hex(f)}:", byte_str)
    except:
        pass

print("Length", len(k1s))

print("==================================")
print(">> Pos 2")

k2s = []
pos = 2
for k1 in k1s:
    for k2 in range(1, 256):
        k = k0 + k1 * (0x100) + k2 * (0x10000)
        f = result + k * modulo

        try:
            hex_str = hex(f)[2:]
            byte_str = bytes.fromhex(hex_str)
            if (byte_str[::-1])[2] in printable:
                k2s.append(k2)
                print(f"\rFound pos={pos}, k={hex(k)}, f={hex(f)}:", byte_str)
        except:
            pass

print("Length", len(k2s))

