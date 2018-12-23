#!/usr/bin/env python3

import requests

def get_output(in_text):
	res = requests.get('http://199.247.6.180:12005/?page=' + in_text)
	return res.text.strip().split('\n')[-1].split('</p>')[0]


for x in range(0, 1000):
	try:
		y = get_output(f'{x}')
		bbb = bytes.fromhex(y)
		print(x, y, bbb)

		if b'X-MAS' in bbb or 'X-MAS' in y:
			quit()
	except:
		pass