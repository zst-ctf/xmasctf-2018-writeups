# Friedrich's Christmas Hangover
Reverse

## Challenge 

	Santa's good friend, Friedrich, got really drunk during a Christmas Eve party and broke the program that verifies his gnomebook password. Now he needs your help because he's still recovering from the hangover.

	chall

	Authors: Gabies + littlewho

## Solution


	$ file chall 
	chall: data

	$ xxd chall | head
	00000000: 7248 414b 0f0c 0c0d 0d0d 0d0d 0d0d 0d0d  rHAK............
	00000010: 0f0d 330d 0c0d 0d0d 0d08 4d0d 0d0d 0d0d  ..3.......M.....
	00000020: 4d0d 0d0d 0d0d 0d0d 9d2b 0d0d 0d0d 0d0d  M........+......
	00000030: 0d0d 0d0d 5d0d 350d 040d 4d0d 160d 170d  ....].5...M.....
	00000040: 0b0d 0d0d 080d 0d0d 4d0d 0d0d 0d0d 0d0d  ........M.......


## Flag

	??