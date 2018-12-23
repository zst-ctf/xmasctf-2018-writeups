#!/usr/bin/env python3
# Probably_Really_Nice_Goodies_from_Santa
# export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:~/Downloads/z3-4.8.0.99339798ee98-x64-osx-10.11.6/bin
# export PYTHONPATH=~/Downloads/z3-4.8.0.99339798ee98-x64-osx-10.11.6/bin/python
from z3 import *

# somehow 32 bits was giving some overflow numbers
BIT_SIZE = 33

iv = z3.BitVec('x', BIT_SIZE)
key = z3.BitVec('y', BIT_SIZE)
mask = z3.BitVec('z', BIT_SIZE)
X = iv
Y = key
Z = mask

s = Solver()

# added this to have full width
s.add(iv >= BitVecVal(0x10000000, BIT_SIZE))
s.add(key >= BitVecVal(0x10000000, BIT_SIZE))
s.add(mask >= BitVecVal(0x10000000, BIT_SIZE))

'''
# added 0xFFFFFFFF due to using 64-bit vectors
s.add(iv <= BitVecVal(0xFFFFFFFF, BIT_SIZE))
s.add(key <= BitVecVal(0xFFFFFFFF, BIT_SIZE))
s.add(mask <= BitVecVal(0xFFFFFFFF, BIT_SIZE))
'''

def parity(x):
	x ^= LShR(x, 16) # x >> 16
	x ^= LShR(x, 8) # x >> 8
	x ^= LShR(x, 4) # x>> 4
	x ^= LShR(x, 2) # x>> 2
	x ^= LShR(x, 1) # x>> 1
	return x & 1

def LFSR():
	global iv
	return (LShR(iv, 1)) | (parity(iv&key) << 32)
	#return self.iv >> 1 | (self.parity(self.iv&self.key) << 32)

def next():
	global iv
	iv = LFSR()

def next_byte():
	global iv
	global mask
	x = iv ^ mask
	next()
	x ^= LShR(x, 16) # x >> 16
	x ^= LShR(x, 8) # x >> 8
	return (x & 255)

def forward_solve(_iv, _key, _mask, _size):
	s.add(iv == BitVecVal(_iv, BIT_SIZE))
	s.add(key == BitVecVal(_key, BIT_SIZE))
	s.add(mask == BitVecVal(_mask, BIT_SIZE))
	for x in range(_size):
		gg = z3.BitVec('a['+str(x)+']', BIT_SIZE)
		s.add(gg == next_byte())

def reverse_solve(val):
	for v in val:
		if v > 0:
			s.add(next_byte() == v)
		else:
			next_byte()

# Test values which I generated.
# `val` should be equal to forward solution
'''
forward_solve(
	_iv=0xd6f45b05,
	_key=0x875f622d,
	_mask=0x434c1fe3,
	_size=30
)
'''
#val = [143, 77, 172, 92, 36, 152, 198, 105, 190, 213, 224, 122, 183, 209, 98, 59, 151, 193, 106, 63, 149, 192, 234, 255, 245, 112, 178, 211, 227, 123]
#reverse_solve(val)


ciphertext = "ab38abdef046216128f8ea76ccfcd38a4a8649802e95f817a2fc945dc04a966d502ef1e31d0a2d"
ciphertext = bytes.fromhex(ciphertext)
val = [243, 21, 230, 159, 163, 61, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 80]
def reverse_solve2(val, ciphertext):
	for i, v in enumerate(val):
		xor_byte = next_byte()
		if v > 0:
			s.add(xor_byte == v)
		else:
			# assert the orig text is printable
			pt = ciphertext[i] ^ xor_byte
			constrain = z3.And(ULT(31, pt), ULT(pt, 127))
			s.add(constrain)
			# https://stackoverflow.com/questions/45066049/what-values-can-be-represented-with-bitvecs-in-z3
			#s.add(31 < pt)
			#s.add(pt < 127)

# Actual solution

reverse_solve2(val, ciphertext)
'''
forward_solve(
	_iv=0xc2f6ec63,
	_key=0x6b924261,
	_mask=0x82fa90a0,
	_size=len(val)
)
'''



print("==========================")
print(s.check())
print(s.model())
print("==========================")
try:
	print( 'iv', hex(int(str(s.model()[X]))) )
except:
	pass

try:
	print( 'key', hex(int(str(s.model()[Y]))) )
except:
	pass

try:
	print( 'mask', hex(int(str(s.model()[Z]))) )
except:
	pass
