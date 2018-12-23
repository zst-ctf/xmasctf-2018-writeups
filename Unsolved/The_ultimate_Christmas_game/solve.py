#!/usr/bin/env python3
import socket
import re
from hashlib import md5

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


human_takeover = True
if __name__ == '__main__':
    s = socket.socket()
    s.connect(('199.247.6.180', 14002))
    while True:
        data = s.recv(4096).decode()
        if not data:
            break

        print("Received:", data)

        if 'Give a string X such that' in data:
            match = re.findall(r'=(.+)\.', data)[0]
            print(">> Lookup", match)
            found, md5hash = lookup(match)
            s.send(found + b'\n')
            print(">> Sending", found)

        if 'Current state of the game: ' in data:
            arr = re.findall(r': (\[.+\])', data)[0]
            arr = eval(arr)

            try:
                last_i, last_item = next((i, s) for i, s in (list(enumerate(arr))) if s > 1)
            except StopIteration:
                human_takeover = True

        if 'Input the pile:' in data:
            if human_takeover == False:
                last_item -= 1
                print(f">> Sending: index {last_i} / quantity {last_item}")
                s.send(str(last_i).encode() + b'\n')
                s.send(str(last_item).encode() + b'\n')
            else:
                what = input('>> Your input A:')
                s.send(str(what).encode() + b'\n')

        if 'Input the quantity:' in data:
            if human_takeover == True:
                what = input('>> Your input B:')
                s.send(str(what).encode() + b'\n')


            '''
            if last_i == 1:
                if arr[1] == 2:
                    last_i = 0
                    last_item = arr[0] - 1
                else:
                    last_item = 1
            '''

            '''
            if last_i == 1:
                if arr[0] == 0:
                    # take all
                    pass
                elif arr[0] == 1:
                    # take one at a time
                    last_item = 1
                else:
                    # take from index 0
                    last_i = 0
                    last_item = arr[0] - 1
            '''

            '''
            if last_item > 2:
                last_item -= 2
            else:
                if arr[0] == 1 and arr[1] == 2:
                    last_item = 1
                if arr[0] == 0 and arr[1] == 2:
                    last_item = 2
            '''

            



    # print(lookup('069de'))


    '''
    s = socket.socket()
    s.connect(('xmas-ctf.cf', 14002))


    num = 0
    while True:
        data = s.recv(4096).decode()
        if not data:
            break

        print("Received:", data)

        if 'Enter a integer:' in data:
            s.send(str(num).encode() + b'\n')
            rhs = 'A0 + A1*x + A2*x^2 + A3*x^3 + A4*x^4 + A5*x^5 + A6*x^6'.replace('x', str(num))
            num += 1

        if 'The output is:' in data:

            result = int(data.split(':')[1].strip())
            lhs = str(result)
            # rhs = 'A0 + A1*x + A2*x^2 + A3*x^3 + A4*x^4 + A5*x^5'.replace('x', f'({result})')
            expr = f'-({lhs}) + ({rhs})'
            print(">> Expr:", expr)
            exprs.append(expr)

            if (previous > result):
                print(">> Smaller")
            previous = result

    '''
