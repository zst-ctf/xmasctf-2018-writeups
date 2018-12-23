# Xⁿ-Mas
Crypto

## Challenge 

	Crypto mecha gnomes love random polynomial functions, can you guess what’s hidden in there?

	Server: nc 199.247.6.180 16000

	Author: Gabies

## Solution

Values are constant across all runs

	$ nc 199.247.6.180 16000
	Hello to the most amazing Christmas event. The X^n-Mas!
	You can send at most 50 requests to the server.
	The modulo is 2952826889. Good luck!
	Enter a integer:0
	The output is: 125
	Enter a integer:1
	The output is: 3458
	Enter a integer:2
	The output is: 2101896213
	Enter a integer:3
	The output is: 1132329010
	Enter a integer:4
	The output is: 1753454089
	Enter a integer:5
	The output is: 717308544
	Enter a integer:6
	The output is: 2058650105
	Enter a integer:7
	The output is: 4262699
	Enter a integer:8
	The output is: 1868985171
	Enter a integer:9
	The output is: 2050921933
	Enter a integer:10
	The output is: 1183280008
	Enter a integer:11
	The output is: 1755818551
	Enter a integer:12
	The output is: 45436690
	Enter a integer:13
	The output is: 2604264975
	Enter a integer:14
	The output is: 2325487316
	Enter a integer:15
	The output is: 1501712470
	Enter a integer:

Range

	$ nc 199.247.6.180 16000
	Hello to the most amazing Christmas event. The X^n-Mas!
	You can send at most 50 requests to the server.
	The modulo is 2952826889. Good luck!
	Enter a integer:-1
	Value not in range [0,2952826888]

Equation?

From sending 0, we get the constant

	A0 = 125 = '}'
	Sum(An...A0) = 3458

Assume each polynomial coefficient of the x-term is the flag

	>>> x = list('X-MAS{')
	>>> list(map(lambda a: ord(a), x))
	[88, 45, 77, 65, 83, 123]
	>>> sum([88, 45, 77, 65, 83, 123])
	481

	A[n] = 88
	A[n-1] = 45
	A[n-2] = 77
	A[n-3] = 65
	A[n-4] = 83
	A[n-5] = 123

	A[0] = 125




If we can make it x = 256 = 0x100, 

	$ nc 199.247.6.180 16000
	Hello to the most amazing Christmas event. The X^n-Mas!
	You can send at most 50 requests to the server.
	The modulo is 1705110751. Good luck!
	Enter a integer:256
	The output is: 25741138

So 

	f(256) % 1705110751 = 25741138

	f(256) = 25741138 + k * 1705110751

We need to find `k` such that

	f(256) & 0xFF == 125 == 0x7d

alternatively,

	$ nc 199.247.6.180 16000
	Hello to the most amazing Christmas event. The X^n-Mas!
	You can send at most 50 requests to the server.
	The modulo is 1705110751. Good luck!
	Enter a integer:65536
	The output is: 1252585515

So

	f(65536) % 1705110751 = 1252585515
	f(65536) = 1252585515 + k * 1705110751

	We need to find `k` such that

	f(65536) & 0x00FF == 0x007d


----------------------------

From 0 to 0xFF (inclusive),

	Found k=53



----------------------------



hex(25741138) = 0x188c752




25741138

	




https://ctftime.org/writeup/10587
https://en.wikipedia.org/wiki/Lagrange_polynomial

	

	25*A5 + 16*A4 + 9*A3 + 4*A2 + A1 + A0 = 2101896213

	A0 + A1*x + A2*x^2 + A3*x^3 + A4*x^4 + A5*x^5

## Flag

	??