# A Weird List of Sequences
Misc

## Challenge 

	The oldest gnome in Lapland came around to tell stories of great wonder to everyone in your hometown! However, for you he has something special. He knows you love maths, and so he decided to see how sharp your mind is by giving you weird sequences that only he knows.

	Are you up to the challenge?

	Server: nc 199.247.6.180 14003

## Solution

Given a sequence and we must find the next item

	$ nc 199.247.6.180 14003
	CAPTCHA!!!
	Give a string X such that md5(X).hexdigest()[:5]=e92cb.
	791023
	Ok, you can continue, go on!

	Hello, litlle one! This time the challenge is very random!
	You will be asked 25 questions where you are given the first 30 terms of a random integer sequence and you will have to determine the next term of that sequence!
	Let's start!

	Question number 1!
	Here's the sequence:
	[1, 1, 1, 5, 1, 9, 1, 25, 5, 9, 1, 65, 1, 9, 9, 125, 1, 65, 1, 65, 9, 9, 1, 425, 5, 9, 25, 65, 1, 121]
	input an integer:

	1
	Good job, next question!

To cheat a little, let us use [*The On-Line Encyclopedia of Integer Sequences*](http://oeis.org/search?q=) to help us...

	$ python3 solve.py

	Received: Question number 25!
	Here's the sequence:

	Received: [1, 16, 104, 344, 792, 1528, 2632, 4152, 6200, 8792, 12072, 16024, 20824, 26424, 33032, 40568, 49272, 59032, 70120, 82392, 96152, 111224, 127944, 146104, 166072, 187608, 211112, 236312, 263640, 292792]
	input an integer:

	>> Sequence 1, 16, 104, 344, 792, 1528, 2632, 4152, 6200, 8792, 12072, 16024, 20824, 26424, 33032, 40568, 49272, 59032, 70120, 82392, 96152, 111224, 127944, 146104, 166072, 187608, 211112, 236312, 263640, 292792
	>> Next Item 324232
	Received: Yay, you did it! Here's your flag: X-MAS{OEIS_1s_S4n7a5_f4v0urit3_w3bs1t3}

## Flag

	X-MAS{OEIS_1s_S4n7a5_f4v0urit3_w3bs1t3}
