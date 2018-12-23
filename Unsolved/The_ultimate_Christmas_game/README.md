# The ultimate Christmas game
Misc

## Challenge 

	Santa was challenged by one of his mechagnomes to this weird game. He needs your help to defeat the gnome, who is a master level player of this game!

	Server: nc 199.247.6.180 14002

	Author: Gabies

## Solution

So we have a game where we need to find an MD5 hash to match a pattern

	$ nc xmas-ctf.cf 14002
	CAPTCHA!!!
	Give a string X such that md5(X).hexdigest()[:5]=e2b9a.

In this case, the first 5 chars need to match... This gives us a 1 in 16^5 chance with a simple bruteforce...


After we get pass the captcha, we are faced with a game of Nim
http://www.archimedes-lab.org/How_to_Solve/Win_at_Nim.html


	$ nc xmas-ctf.cf 14002
	CAPTCHA!!!
	Give a string X such that md5(X).hexdigest()[:5]=7f8b4.
	43724
	Ok, you can continue, go on!
	Help Santa win this game against one of his gnomes!
	The rules are simple, choose a non-empty pile of stone and remve from it a positive number of stones.
	The player who takes the last stone wins!
	You start.
	Current state of the game: [88, 18, 88, 26, 3, 27, 64, 66, 76, 25, 48, 35, 56, 59, 32]

	Input the pile:




## Flag

	??