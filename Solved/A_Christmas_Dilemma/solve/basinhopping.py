#!/usr/bin/env python3
import socket
import re
from hashlib import md5
from threading import Thread
from queue import Queue
import functools

from scipy.optimize import basinhopping
from numpy.testing import assert_almost_equal


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


func_queue = Queue(maxsize=1)
result_queue = Queue(maxsize=1)

def start_basinhop(startX, minX, maxX):
    # an example function with multiple minima
    @functools.lru_cache(maxsize=None)
    def f_memo(x):
        # x = x[0]
        func_queue.put((x, True))
        # Wait for results
        x1, result = result_queue.get()
        result_queue.task_done()
        assert_almost_equal(x1, x, decimal=5)
        # basinhopping finds the minimum, so invert
        # the result for maximum point
        return -result

    def f(x):
        # Put x into queue
        x = round(x[0], 6)
        result = f_memo(x)
        return round(result, 6)

    # the starting point
    x0 = [startX, startX]

    # the bounds
    xmin = [minX, minX]
    xmax = [maxX, maxX]

    # rewrite the bounds in the way required by L-BFGS-B
    bounds = [(low, high) for low, high in zip(xmin, xmax)]

    # use method L-BFGS-B because the problem is smooth and bounded
    minimizer_kwargs = dict(method="L-BFGS-B", bounds=bounds)
    res = basinhopping(
        f, x0, 
        stepsize=1,
        interval=5,
        # Maximum of 500 iterations, stop if remains same for 30 successions
        niter=50, #niter_success=20,
        minimizer_kwargs=minimizer_kwargs)
    
    # End off by sending result
    # normalise it back
    optimisedX = res.x[0]
    optimisedY = -f(res.x)
    func_queue.put((optimisedY, False))
    return res


def main():
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
            minX = float(found[0]) + 0.001
            maxX = float(found[1]) - 0.001
            startX = (maxX + minX) / 2
            queries = 0

            # Start of the program, define these
            thread = Thread(target=start_basinhop, args=(startX, minX, maxX))
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
                s.send(str(numb).encode() + b'\n')
                print(f">> Guessing {numb}")

            func_queue.task_done()

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

if __name__ == '__main__':
    main()


            
            