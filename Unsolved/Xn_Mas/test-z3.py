#!/usr/bin/env python3
# Xn_Mas
# export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:~/Downloads/z3-4.8.0.99339798ee98-x64-osx-10.11.6/bin
# export PYTHONPATH=~/Downloads/z3-4.8.0.99339798ee98-x64-osx-10.11.6/bin/python
from z3 import *

def solve(N):
    s = Solver()
    A = IntVector("A", N+1)

    def add_function(x, y):
        # Add a polynominal function
        # of order `n`, such that f(`x`) = `y`
        output = 0
        for i in range(N+1):
            output += A[i] * (x**i)
        s.add((output % 2952826889) == y)

    eqz = [
        # (0, 125),
        (1, 3458),
        (2, 2101896213),
        (3, 1132329010),
        (4, 1753454089),
        (5, 717308544),
        (6, 2058650105),
        (7, 4262699),
        (8, 1868985171),
        (9, 2050921933),
        (10, 1183280008),
        (11, 1755818551),
        (12, 45436690),
        (13, 2604264975),
        (14, 2325487316),
        (15, 1501712470),
    ]

    for eq in eqz:
        x = eq[0]
        y = eq[1]
        add_function(x, y)

    # 'X-MAS{' and '}'
    s.add(A[N]   == 88)
    s.add(A[N-1] == 45)
    s.add(A[N-2] == 77)
    s.add(A[N-3] == 65)
    s.add(A[N-4] == 83)
    s.add(A[N-5] == 123)
    s.add(A[0]   == 125)

    print(">>Check model")
    print(f'N = {N}, model = {str(s.check())}')
    if str(s.check()) == 'sat':
        m = s.model()
        print(m)
        #print(f'A[{i}]', )
        # rint( 'iv', hex(int(str(s.model()[X]))) )

if __name__ == '__main__':
    for _n in range(6, 100):
        solve(_n)
