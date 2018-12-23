#!/usr/bin/env python
from __future__ import print_function
from pwn import *

# Must be in Python 2.7
assert hash('admin') == -5290733415256081176

# Do hash lookup table
lookup_table = dict()
for num in xrange(9999999):
	if num & 0xFFFFF == 1:
		print('\r', num, end='')
	num = '%07d' % num
	
	# before
	text = num + 'stealer'
	lookup_table[hash(text)] = text

	# after
	text = 'stealer' + num
	lookup_table[hash(text)] = text


def lookup(t):
	return lookup_table[t]

print('\nDone Lookup')

# Connect to server
p = remote('199.247.6.180', 18000)

# (1) Solve riddle
log.info('>> Part 1')
# https://riddles.fyi/if-you-want-me-youll-have-to-share-me-but-if-you-share-me-i-will-be-gone-what-am-i/
p.recvuntil('What am I?(one word)')
p.sendline('secret')

# (2) Crack hashes
log.info('>> Part 2')
p.recvuntil('Anyway here are the hashes:')
while True:
	line = p.recvline().strip()
	if not line:
		continue

	log.info(line)

	if 'Congrats! Moving to the next task' in line:
		break

	hash_num = int(line)
	text = lookup(hash_num)
	print('>>', hash_num, '->', text)
	p.sendline(text)

# (3) how many reindeers are in this image
log.info('>> Part 3')
p.recvuntil('You should send me ')
line = p.recvline().strip()

# convert to python friendly equation & eval answer
no_of_reindeers=17
equation = line.replace('^', '**').replace(' ', '')
answer = str(eval(equation))

log.info(answer)
p.sendline(answer)

# (4) I need a password so I can see where the reindeers are trapped at
log.info('>> Part 4')
p.recvuntil('https://pasteboard.co/HRwM0jU.png')
p.sendline('sternocleidomastoidian')

log.info('>> Part 5')
p.sendline('this_is_not_a_red_herring')
p.interactive()
