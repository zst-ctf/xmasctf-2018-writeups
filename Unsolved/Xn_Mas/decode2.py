#!/usr/bin/env python3
import string
printable = bytes(string.ascii_letters + string.digits + '!"#$%&\'()*+,-./:;?@[\\]^_`{|}~', 'ascii')


modulo = 1705110751
result = 25741138

f0 = 125
f1 = 3458

print("==================================")
print(">> Pos 0")

def get_k0():
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
    return k0


def do_position(pos, k1s):
    k2s = []
    for k1 in k1s:
        for k2 in range(256):
            k = k1 + (k2 << (8*pos))
            f = result + k * modulo

            try:
                current_byte = (f >> (8*pos)) & 0xFF
                #hex_str = hex(f)[2:]
                #byte_str = bytes.fromhex(hex_str)
                #if (byte_str[::-1])[pos] in printable:
                if current_byte in printable:
                    k2s.append(k)
                    byte_str = bytes.fromhex(hex(f)[2:])
                    # print(f"\rFound pos={pos}, k={hex(k)}, f={hex(f)}:", byte_str)

                if b'X-MAS{' in byte_str:
                    quit()
            except:
                pass
    return k2s


if __name__ == '__main__':
    print("==================================")
    print(f">> Initial Pos")
    k0 = get_k0()

    kXs = [k0]
    for pos in range(1, 10):
        print("==================================")
        print(f">> Start Pos {pos} ")
        kXs = do_position(pos, kXs)
        print(f">> Done Pos {pos} -> Length {len(kXs)}", )


