from __future__ import print_function
import os

flag = "X-MAS{TESTING_TESTING_TESTING}" #open('flag.txt').read().strip()

class PRNG():
	def __init__(self):
		self.seed = self.getseed()
		self.iv = int(bin(self.seed)[2:].zfill(64)[0:32], 2)
		self.key = int(bin(self.seed)[2:].zfill(64)[32:64], 2)
		self.mask = int(bin(self.seed)[2:].zfill(64)[64:96], 2)
		self.aux = 0

		print("Seed:", hex(self.seed)) # seed is 12 bytes or 96 bits
		print("IV:", hex(self.iv))  # first 32 bits
		print("Key:", hex(self.key))  # middle 32 bits
		print("Mask:", hex(self.mask))  # last 32 bits

	def parity(self,x):
		# parity bit using 0,1,2,4,8,16th index positions
		x ^= x >> 16
		x ^= x >> 8
		x ^= x>> 4
		x ^= x>> 2
		x ^= x>> 1
		return x & 1
	
	def getseed(self):
		return int(os.urandom(12).encode('hex'), 16)
	
	def LFSR(self):
		return self.iv >> 1 | (self.parity(self.iv&self.key) << 32)
	
	def next(self):
		self.aux, self.iv = self.iv, self.LFSR()
	
	def next_byte(self):
		# IV XOR MASK
		# then for each byte in x, XOR together
		# M4^M3^M2^M1 ^ (A4^A3^A2^A1)
		# M4^M3^M2^M1 ^ (B4^B3^B2^B1)
		# M4^M3^M2^M1 ^ (C4^C3^C2^C1)
		# M4^M3^M2^M1 ^ (D4^D3^D2^D1)
		# M4^M3^M2^M1 ^ (E4^A4^A3^A2) = M4^M3^M2^M1 ^ (E4^E3^E2^E1)
		# M4^M3^M2^M1 ^ (F4^B4^B3^B2) = M4^M3^M2^M1 ^ (F4^F3^F2^F1)
		x = self.iv ^ self.mask
		self.next()
		x ^= x >> 16
		x ^= x >> 8
		return (x & 255)

prng_bytes = []
def encrypt(s):
	o=''
	for i, x in enumerate(s):
		prng = p.next_byte()
		encr = chr(ord(x) ^ prng)
		o += encr
		print("Index: {:02d} | Char: 0x{:02x} | PRNG: 0x{:02x} | Encrypt: 0x{:02x}".format(
			i, ord(x), prng, ord(encr)))
		prng_bytes.append(prng)
		
	return o.encode('hex')

p=PRNG()

print("encrypted:", encrypt(flag))
print("prng_bytes:", prng_bytes)
#with open('flag.enc','w') as f:
#	f.write(encrypt(flag))

print("=======================================")

prng_bytes = []
def decrypt():
	ciphertext = "ab38abdef046216128f8ea76ccfcd38a4a8649802e95f817a2fc945dc04a966d502ef1e31d0a2d"
	ciphertext = ciphertext.decode('hex')

	print("Length:", len(ciphertext))

	orig_text = "X-MAS{" + "\x00"*(len(ciphertext) - 6 - 1) + "}"
	assert len(ciphertext) == len(orig_text)
	for i, (a,b) in enumerate(zip(orig_text, ciphertext)):
		orig = ord(a)
		encr = ord(b)
		xor = orig ^ encr
		if orig > 0:
			prng_bytes.append(xor)
		else:
			prng_bytes.append(-1)

		print("Index: {:02d} | Encrypt: 0x{:02x} | Char: 0x{:02x} | PRNG: 0x{:02x}".format(
			i, encr, orig, xor))

decrypt()
print("prng_bytes:", prng_bytes)

