#!/usr/bin/env python3

ciphertext = "ab38abdef046216128f8ea76ccfcd38a4a8649802e95f817a2fc945dc04a966d502ef1e31d0a2d"
ciphertext = bytes.fromhex(ciphertext)
print("Length:", len(ciphertext))

def decrypt(ciphertext, xor_key):
    assert len(ciphertext) == len(xor_key)
    final = ''
    for i, (a, b) in enumerate(zip(ciphertext, xor_key)):
        orig = a ^ b
        final += chr(orig)
    print(final)

# Empty XOR key
a = [0] * len(ciphertext)

# Values of XOR key
a[38] = 80
a[37] = 121
a[36] = 42
a[35] = 140
a[34] = 193
a[33] = 90
a[32] = 108
a[31] = 1
a[30] = 218
a[29] = 109
a[28] = 2
a[27] = 220
a[26] = 97
a[25] = 26
a[24] = 236
a[23] = 0
a[22] = 216
a[21] = 104
a[20] = 8
a[19] = 200
a[18] = 72
a[17] = 73
a[16] = 75
a[15] = 78
a[14] = 69
a[13] = 83
a[12] = 126
a[11] = 37
a[10] = 147
a[9] = 255
a[8] = 38
a[7] = 149
a[6] = 242
a[5] = 61
a[4] = 163
a[3] = 159
a[2] = 230
a[1] = 21
a[0] = 243

a = bytes(a)

decrypt(ciphertext, a)


