#!/usr/bin/env python3
import binascii
from PIL import Image

filename = 'suspicious.png'
img = Image.open(filename).convert('RGB')
pixels = img.load()
width, height = img.size


bottom_height = 1307

with open('output.dat', 'wb') as f:
	f.write(b'')

for y in range((height - 1) - bottom_height, height):
	print(f'\r y={y} of {height}', end='')
	hidden_data = b''
	for x in range(0, width):
		r, g, b = pixels[x, y]
		hidden_data += bytes([r ^ g ^ b])
	with open('output.dat', 'ab') as f:
		f.write(hidden_data)
print(f'\nDone')
