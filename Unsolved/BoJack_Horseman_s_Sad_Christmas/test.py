#!/usr/bin/env python3
import binascii
from PIL import Image


# https://stackoverflow.com/questions/11599226/how-to-convert-binary-string-to-ascii-string-in-python
def bin_to_ascii(bin_text, size=8):
    return ''.join(chr(int(bin_text[i:i+size], 2)) for i in range(0, len(bin_text), 8))

filename = 'bojack.png'
img = Image.open(filename).convert('RGB')
pixels = img.load()
width, height = img.size



white_consecutive = 0
bojack = []
for y in range(0, height):
	for x in range(0, width):
		r, g, b = pixels[x, y]
		print(hex(r), hex(g), hex(b))

		bojack.append(f"{hex(r)}, {hex(g)}, {hex(b)}")

print(list(set(bojack)))

output = ''
for col in bojack:
	if col == '0xbf, 0xb, 0xb':
		output += '0'
	else:
		output += '1'


		'''
		#output += '1' if ((r ^ g ^ b) & 0x01 == 1) else '0'
		output += '1' if (b & 0x01 == 1) else '0'
		output += '1' if (g & 0x01 == 1) else '0'
		output += '1' if (r & 0x01 == 1) else '0'

		# output += '1' if (v & 0x01 == 1) else '0'

		if (r & 1 == 1) and (g & 1 == 1) and (b & 1 == 1):
			white_consecutive += 1
		else:
			white_consecutive = 0
		if white_consecutive >= 8:
			break
		'''





orig_output = output
for x in range(0, 8+1):
	output = ((orig_output[x:]))
	print("=============================================")
	print(output)
	print("Length", len(output))
	print('%x' % int(output, 2))
	print("=============================================")
	print(bin_to_ascii(output, 7))
	print("=============================================")
	try:
		msg = binascii.unhexlify('%x' % int(output, 2))
		print(msg.decode(errors='ignore'))
	except:
		msg = binascii.unhexlify('%x0' % int(output, 2))
		print(msg.decode(errors='ignore'))
		print('OR')
		msg = binascii.unhexlify('0%x' % int(output, 2))
		print(msg.decode(errors='ignore'))
	quit()
