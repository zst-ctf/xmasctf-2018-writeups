# Let's Crack the Great lapland monolith
Web/Crypto

## Challenge 

	"Psst, I got a task for you. There's this monolith to which I need to get access, but I can't get the numbers right. Can you help me? I pay well." ~ A shady dealer gnome

	Server: http://199.247.6.180:12000

	Authors: Milkdrop + Gabies

## Solution

From the title, we know this is an [Linear congruential generator, LCG,](https://en.wikipedia.org/wiki/Linear_congruential_generator) challenge.

Let's refer to my past challenge writeups:

1. [angstromctf 2018 - ofb](https://github.com/zst123/angstromctf-2018-writeups/tree/master/Solved/ofb)
2. [gryphonctf 2018 - Lupusregina](https://github.com/zst123/gryphonctf-2018-writeups/tree/master/Solved/Lupusregina)

### What we need to do

We can generate any amount of lcg values, however, we do not have the modulus.

My past scripts can be used as it is, but I need to add a portion to get the modulus

To solve this, I generated lcg_0 through lcg_2.. Then I did a bruteforce of the modulus. The lcg_3 value is used to verify until the modulus is guessed correctly.

### Solving

	$ python3 solve.py 
	
	// MONOLITH ACCESS POINT
	// You Guessed: 0 The Monolith desired: 43638 Wrong guess! Streak: 0
	// MONOLITH ACCESS POINT
	// You Guessed: 0 The Monolith desired: 39823 Wrong guess! Streak: 0
	// MONOLITH ACCESS POINT
	// You Guessed: 0 The Monolith desired: 47997 Wrong guess! Streak: 0
	// MONOLITH ACCESS POINT
	// You Guessed: 0 The Monolith desired: 34729 Wrong guess! Streak: 0
	Retrieved:
	>> lcg_0: 43638
	>> lcg_1: 39823
	>> lcg_2: 47997
	>> lcg_3: 34729

	Found parameters:
	>> mod: 51913
	>> a: 32833
	>> c: 20256

	Doing guesses:
	>> next 0: 8468
	// MONOLITH ACCESS POINT
	// You Guessed: 8468 The Monolith desired: 8468 Correct guess! Streak: 1
	>> next 1: 4072
	// MONOLITH ACCESS POINT
	// You Guessed: 4072 The Monolith desired: 4072 Correct guess! Streak: 2
	>> next 2: 40257
	// MONOLITH ACCESS POINT
	// You Guessed: 40257 The Monolith desired: 40257 Correct guess! Streak: 3
	>> next 3: 21444
	// MONOLITH ACCESS POINT
	// You Guessed: 21444 The Monolith desired: 21444 Correct guess! Streak: 4
	>> next 4: 47002
	// MONOLITH ACCESS POINT
	// You Guessed: 47002 The Monolith desired: 47002 Correct guess! Streak: 5
	>> next 5: 19171
	// MONOLITH ACCESS POINT
	// You Guessed: 19171 The Monolith desired: 19171 Correct guess! Streak: 6
	>> next 6: 16574
	// MONOLITH ACCESS POINT
	// You Guessed: 16574 The Monolith desired: 16574 Correct guess! Streak: 7
	>> next 7: 42332
	// MONOLITH ACCESS POINT
	// You Guessed: 42332 The Monolith desired: 42332 Correct guess! Streak: 8
	>> next 8: 40063
	// MONOLITH ACCESS POINT
	// You Guessed: 40063 The Monolith desired: 40063 Correct guess! Streak: 9
	>> next 9: 37141
	// MONOLITH ACCESS POINT
	// You Guessed: 37141 The Monolith desired: 37141 Correct guess! Streak: 10
	>> next 10: 34339
	// MONOLITH ACCESS POINT
	// You Guessed: 34339 The Monolith desired: 34339 Correct guess! Streak: 11
	>> next 11: 26109
	// MONOLITH ACCESS POINT
	// You Guessed: 26109 The Monolith desired: 26109 Correct guess! Streak: 12
	>> next 12: 17684
	// MONOLITH ACCESS POINT
	// You Guessed: 17684 The Monolith desired: 17684 Correct guess! Streak: 13
	>> next 13: 44036
	// MONOLITH ACCESS POINT
	// You Guessed: 44036 The Monolith desired: 44036 Correct guess! Streak: 14
	>> next 14: 25281
	// MONOLITH ACCESS POINT
	// You Guessed: 25281 The Monolith desired: 25281 Correct guess! Streak: 15
	>> next 15: 34372
	// MONOLITH ACCESS POINT
	// You Guessed: 34372 The Monolith desired: 34372 Correct guess! Streak: 16
	>> next 16: 19425
	// MONOLITH ACCESS POINT
	// You Guessed: 19425 The Monolith desired: 19425 Correct guess! Streak: 17
	>> next 17: 50076
	// MONOLITH ACCESS POINT
	// You Guessed: 50076 The Monolith desired: 50076 Correct guess! Streak: 18
	>> next 18: 28941
	// MONOLITH ACCESS POINT
	// You Guessed: 28941 The Monolith desired: 28941 Correct guess! Streak: 19
	>> next 19: 24557
	// MONOLITH ACCESS POINT
	// You Guessed: 24557 The Monolith desired: 24557 Correct guess! Streak: 20 Congratulations! Here's your flag: X-MAS{LCG_0n_7h3_LapL4nd_m0n0LiTh_1s_n0t_7ha7_s3cur3}
	>> next 20: 39434
	// MONOLITH ACCESS POINT
	// You Guessed: 39434 The Monolith desired: 39434 Correct guess! Streak: 21 Congratulations! Here's your flag: X-MAS{LCG_0n_7h3_LapL4nd_m0n0LiTh_1s_n0t_7ha7_s3cur3}
	>> next 21: 46558
	// MONOLITH ACCESS POINT
	// You Guessed: 46558 The Monolith desired: 46558 Correct guess! Streak: 22 Congratulations! Here's your flag: X-MAS{LCG_0n_7h3_LapL4nd_m0n0LiTh_1s_n0t_7ha7_s3cur3}
	>> next 22: 28872
	// MONOLITH ACCESS POINT
	// You Guessed: 28872 The Monolith desired: 28872 Correct guess! Streak: 23 Congratulations! Here's your flag: X-MAS{LCG_0n_7h3_LapL4nd_m0n0LiTh_1s_n0t_7ha7_s3cur3}
	>> next 23: 43252
	// MONOLITH ACCESS POINT
	// You Guessed: 43252 The Monolith desired: 43252 Correct guess! Streak: 24 Congratulations! Here's your flag: X-MAS{LCG_0n_7h3_LapL4nd_m0n0LiTh_1s_n0t_7ha7_s3cur3}
	>> next 24: 33057
	// MONOLITH ACCESS POINT
	// You Guessed: 33057 The Monolith desired: 33057 Correct guess! Streak: 25 Congratulations! Here's your flag: X-MAS{LCG_0n_7h3_LapL4nd_m0n0LiTh_1s_n0t_7ha7_s3cur3}
	>> next 25: 35646
	// MONOLITH ACCESS POINT
	// You Guessed: 35646 The Monolith desired: 35646 Correct guess! Streak: 26 Congratulations! Here's your flag: X-MAS{LCG_0n_7h3_LapL4nd_m0n0LiTh_1s_n0t_7ha7_s3cur3}
	>> next 26: 6789
	// MONOLITH ACCESS POINT
	// You Guessed: 6789 The Monolith desired: 6789 Correct guess! Streak: 27 Congratulations! Here's your flag: X-MAS{LCG_0n_7h3_LapL4nd_m0n0LiTh_1s_n0t_7ha7_s3cur3}
	>> next 27: 9071
	// MONOLITH ACCESS POINT
	// You Guessed: 9071 The Monolith desired: 9071 Correct guess! Streak: 28 Congratulations! Here's your flag: X-MAS{LCG_0n_7h3_LapL4nd_m0n0LiTh_1s_n0t_7ha7_s3cur3}
	>> next 28: 23518
	// MONOLITH ACCESS POINT
	// You Guessed: 23518 The Monolith desired: 23518 Correct guess! Streak: 29 Congratulations! Here's your flag: X-MAS{LCG_0n_7h3_LapL4nd_m0n0LiTh_1s_n0t_7ha7_s3cur3}
	>> next 29: 32788
	// MONOLITH ACCESS POINT
	// You Guessed: 32788 The Monolith desired: 32788 Correct guess! Streak: 30 Congratulations! Here's your flag: X-MAS{LCG_0n_7h3_LapL4nd_m0n0LiTh_1s_n0t_7ha7_s3cur3}


## Flag

	X-MAS{LCG_0n_7h3_LapL4nd_m0n0LiTh_1s_n0t_7ha7_s3cur3}
