#!/usr/bin/env python3
import socket
import re
from hashlib import md5
from threading import Thread
from multiprocessing import Queue
import functools
import time

from numpy.testing import assert_almost_equal

# git clone https://github.com/paulknysh/blackbox
import blackbox as bb

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

# Multiprocessing Queues
# https://stackoverflow.com/questions/925100/python-queue-multiprocessing-queue-how-they-behave
func_queue = Queue(maxsize=1)
result_queue = Queue(maxsize=1)


# Implement function connected to the server API
# The queues above are used to pass data between the 
# blackbox optimiser and the main (to server) threads
@functools.lru_cache(maxsize=None)
def f_memo(x):
    global func_queue
    global result_queue
    # x = x[0]
    func_queue.put((x, True))
    print(f"@@ Entered func_queue.put1 ({x})")
    # Wait for results
    x1, result = result_queue.get()
    # result_queue.task_done()
    assert_almost_equal(x1, x, decimal=5)
    print("@@ Received func results")
    # library finds the minimum, so invert
    # the result for maximum point
    return -result


def func(x):    
    # Put x into queue
    x = x[0]
    result = f_memo(x)
    return result


def start_blackbox_optimise(minX, maxX):
    bb.search(f=func,  # given function
              box=[[minX, maxX]],  # range of values for each parameter (2D case)
              n=10,  # number of function calls on initial stage (global search)
              m=40,  # number of function calls on subsequent stage (local search)
              batch=2,  # number of calls that will be evaluated in parallel
              resfile='output.csv')  # text file where results will be saved
    print("@@ Done blackbox search")

    # End off by sending result
    with open('output.csv', 'r') as f:
        # line zero is the header, line one is the best result
        line1 = f.readlines()[1]
    x1, y1 = eval(line1)

    # remember to invert back the y value
    optimised = -y1
    func_queue.put((optimised, False))


def main():
    global func_queue
    global result_queue
    s = socket.socket()
    s.connect(('199.247.6.180', 14001))
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

        """
        This Christmas' dilemma is:
        Given a random function defined in range (-39, 109) find the global maximum of the function!
        You can send at most 501 queries including guesses.
        The guessed value must be equal to the real answer up to 2 decimals.
        """
        if 'Given a random function defined in range' in data:
            found = re.findall(r'range \((.+), (.+)\)', data)[0]
            minX = float(found[0])
            maxX = float(found[1])
            queries = 0

            # Start of the program            
            thread = Thread(target=start_blackbox_optimise, args=(minX, maxX))
            thread.start()

        """
        Choose your action:
        [1] Query the value of the function at some point
        [2] Guess the global maximum
        """
        if 'Choose your action:' in data:
            # get from queue
            numb, action = func_queue.get()

            if action:
                s.send(b'1\n')
                s.send(str(numb).encode() + b'\n')
                print(f">> Querying {numb}")
                queries += 1

            else:
                s.send(b'2\n')

        if 'Enter your guess' in data:
            s.send(str(numb).encode() + b'\n')
            print(f">> Guessing {numb}")
            break


        # f(60.727989) = 28.1988994306
        if 'f(' in data:
            grp = re.findall(r'f\((.+)\) = (.+)', data)[0]
            x = float(grp[0])
            y = float(grp[1])
            print(f">> Did {queries} queries, f({x}) = {y}")
            result_queue.put((x, y))

    while True:
        data = s.recv(4096).decode()
        if not data:
            break

        print("Received:", data)
        if 'Choose your action:' in data:
            s.send(b'2\n')
            queries += 1

        if 'Enter your guess' in data:
            numb += 0.01
            s.send(str(numb).encode() + b'\n')
            print(f">> Guessing {numb}")

        if "Nope, that's quite far away from the real answer" in data:
            print(f">> Did {queries} queries, guessing mode")

        if 'X-MAS{' in data:
            quit()

    '''
    while True:
        data = s.recv(4096).decode()
        if not data:
            break

        print("Received:", data)
        if 'Enter your' in data or 'Choose your' in data:
            what = input('**:')
            s.send(str(what).encode() + b'\n')
    '''

if __name__ == '__main__':
    main()
           