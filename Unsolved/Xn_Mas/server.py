#!/usr/bin/env python3
import socket
import time
import string
import re


modulo = 508117637
previous = 0
exprs = []

if __name__ == '__main__':
    s = socket.socket()
    s.connect(('199.247.6.180', 16000))

    num = 0
    while True:
        data = s.recv(4096).decode()
        if not data:
            break

        print("Received:", data)

        if 'Enter a integer:' in data:
            s.send(str(num).encode() + b'\n')
            #rhs = 'A0 + A1*x + A2*x^2 + A3*x^3 + A4*x^4 + A5*x^5 + A6*x^6'.replace('x', str(num))
            

        if 'The output is:' in data:
            result = int(data.split(':')[1].strip())
            print(f"f{num} = ", result)

            num += 1
            #lhs = str(result)
            # rhs = 'A0 + A1*x + A2*x^2 + A3*x^3 + A4*x^4 + A5*x^5'.replace('x', f'({result})')
            #expr = f'-({lhs}) + ({rhs})'
            #print(">> Expr:", expr)
            #exprs.append(expr)

            #if (previous > result):
            #    print(">> Smaller")
            #previous = result
