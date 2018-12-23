#!/usr/bin/env python3
import requests
import gmpy2
from bs4 import BeautifulSoup

# LCG solver
def lcg(m, a, c, x=0):
    return (a * x + c) % m

def rlcg(m, a, c, x=0):
    ainv = gmpy2.invert(a, m)
    return ainv * (x - c) % m

def solve_a(lcg0, lcg1, lcg2, m):
    a = (lcg2 - lcg1) * gmpy2.invert(lcg1 - lcg0, m) % m
    return a

def solve_c(lcg0, lcg1, m, a):
    c = (lcg1 - a * lcg0) % m
    return c

session = requests.session()

# API functions
def guess(num=0):
	url = f'http://199.247.6.180:12006/?guess={num}'
	res = session.get(url=url)

	soup = BeautifulSoup(res.text, 'html.parser')
	for paragraph in soup.select('form > p'):
		paragraph = paragraph.get_text(strip=True, separator=" ")

		if 'The Monolith desired:' in paragraph:
			desired = paragraph.split('The Monolith desired: ', 1)[1].split(' ', 1)[0]
			desired = int(desired.strip())

		print('// ' + paragraph)
	
	return desired


def main():
	# Get lcg values original
	lcg_0 = guess()
	lcg_1 = guess()
	lcg_2 = guess()
	lcg_3 = guess()
	print(f'Retrieved:')
	print(f'>> lcg_0: {lcg_0}')
	print(f'>> lcg_1: {lcg_1}')
	print(f'>> lcg_2: {lcg_2}')
	print(f'>> lcg_3: {lcg_3}')
	print()

	# Find the mod value
	modulus = -1
	for mod_value in reversed(range(30000, 2**16)):
		try:
			a = solve_a(lcg_0, lcg_1, lcg_2, mod_value)
			c = solve_c(lcg_0, lcg_1, mod_value, a)
			next = lcg(mod_value, a, c, lcg_2)

			if next == lcg_3:
				modulus = mod_value
				break
		except ZeroDivisionError:
			pass

	# Now we have all the parameters
	print(f'Found parameters:')
	print(f'>> mod: {modulus}')
	print(f'>> a: {a}')
	print(f'>> c: {c}')
	print()

	print(f'Doing guesses:')
	lcg_last = lcg_3
	for x in range(30):
		lcg_last = lcg(mod_value, a, c, lcg_last)
		print(f'>> next {x}: {lcg_last}')
		guess(lcg_last)



if __name__ == '__main__':
	main()
