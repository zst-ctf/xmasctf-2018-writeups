#!/usr/bin/env python3
import socket
import re
import requests
from hashlib import md5

# Lookup for hash captcha
cache = dict()

def lookup(match):
    for X in range(16**6):
        X = str(X).encode()

        if X not in cache:
            cache[X] = md5(X).hexdigest()
            print('New:', X, cache[X])

        md5sum = cache[X]
        if md5sum[:5] == match:
            return (X, cache[X])


def oeis(seq):
    seq = seq.replace(' ', '')
    res = requests.get("http://oeis.org/search?q=" + seq)

    found = re.search(r'<tt><b.+</b>,(.+?),', res.text)
    next_seq = found.group(1).strip()
    return next_seq


def main():
    s = socket.socket()
    s.connect(('199.247.6.180', 14003))
    while True:
        data = s.recv(4096).decode()
        if not data:
            break

        print("Received:", data)

        if 'CAPTCHA!!!' in data:
            match = re.findall(r'=(.+)\.', data)[0]
            print(">> Lookup", match)
            found, md5hash = lookup(match)
            s.send(found + b'\n')
            print(">> Sending", found)
            continue

        #if "Here's the sequence:" in data:
        if "[" in data:
            sequence = re.findall(r'\[(.+)\]', data)[0]
            next_item = oeis(sequence)

            print(">> Sequence", sequence)
            print(">> Next Item", next_item)
            s.send(next_item.encode() + b'\n')
            continue

if __name__ == '__main__':
    # oeis('2, 7, 16, 31, 60, 113, 205, 371, 663, 1176, 2069, 3631, 6341, 11039, 19159, 33164, 57287, 98763, 169967, 292061, 501165, 858892, 1470334, 2514423, 4295912, 7333264, 12508213, 21319360, 36312685, 61811287')
	main()
