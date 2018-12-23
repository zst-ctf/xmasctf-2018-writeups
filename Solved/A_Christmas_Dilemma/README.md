# A Christmas Dilemma
Misc

## Challenge 

	Santa accidentally mixed up his personal Advanced Algebra problem book with a children's book that was supposed to be a present! Now, the algebra book arrived at Little Timmy, who's a math whizz himself. However, he needs your help, because this problem is just too hard for him to solve on his own!

	Server: nc 199.247.6.180 14001

	Author: Gabies

## Solution

We are given a blackbox function and we must find the global maximum.

	$ nc 199.247.6.180 14001
	CAPTCHA!!!
	Give a string X such that md5(X).hexdigest()[:5]=be85c.
	343312
	Ok, you can continue, go on!
	This Christmas' dilemma is:
	Given a random function defined in range (-38, 146) find the global maximum of the function!
	You can send at most 501 queries including guesses.
	The guessed value must be equal to the real answer up to 2 decimals.

	Choose your action:
	[1] Query the value of the function at some point
	[2] Guess the global maximum

	1
	Enter a float: -37
	f(-37.0) = 4.19793289254
	Choose your action:
	[1] Query the value of the function at some point
	[2] Guess the global maximum

	1
	Enter a float: 146
	f(146.0) = 12.5253441935
	Choose your action:
	[1] Query the value of the function at some point
	[2] Guess the global maximum


There are a few algorithms to solve it...

Most of the libraries solve for *optimised global minimum*, hence they can be incorporated into this challenge by inverting the sign of the results - ie. `y = -f(x)`

### Blackbox optimisation solvers

I tried SciPy's basinhopping method to optimise
- https://docs.scipy.org/doc/scipy-0.19.0/reference/generated/scipy.optimize.basinhopping.html
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.basinhopping.html
- https://stackoverflow.com/questions/21670080/how-to-find-global-minimum-in-python-optimization-with-bounds
- https://stackoverflow.com/questions/36782172/scipy-basinhopping-not-respecting-stepsize
- https://esa.github.io/pagmo2/docs/cpp/algorithms/mbh.html

I also found another python [library named blackbox](https://github.com/paulknysh/blackbox) which seems to be a better fit for this challenge. I eventually went with this...

### Solving

Unfortunately, using either method doesn't seem to work at first (telling me that my answer is wrong)...

I decided to change strategy and bruteforce in increments of +0.01 after an initial search...

And with this, both my scripts are working successfully

> [optimise-blackbox.py](./solve/optimise-blackbox.py)

> [basinhopping.py](./solve/basinhopping.py)

Eventually, I got the flag...

	Received: Enter your guess: 
	>> Guessing 48.23799999999989
	Received: Nope, that's quite far away from the real answer.

	>> Did 103 queries, guessing mode
	Received: Choose your action:
	[1] Query the value of the function at some point
	[2] Guess the global maximum


	Received: Enter your guess: 
	>> Guessing 48.24799999999989
	Received: Congratulations! Here's your flag!
	 X-MAS{Th4nk5_for_m4k1ng_a_ch1ld_h4ppy_th1s_Chr1stma5}

	Received: Choose your action:
	[1] Query the value of the function at some point
	[2] Guess the global maximum


	Received: Enter your guess: 
	>> Guessing 48.25799999999989
	Received: Congratulations! Here's your flag!
	 X-MAS{Th4nk5_for_m4k1ng_a_ch1ld_h4ppy_th1s_Chr1stma5}

	Received: Choose your action:
	[1] Query the value of the function at some point
	[2] Guess the global maximum


	Received: Enter your guess: 
	>> Guessing 48.26799999999989
	Received: Nope, that's quite far away from the real answer.

For this case, the blackbox solver did a guess of `47.708`, but the accepted answer is `48.25`

## Flag

	X-MAS{Th4nk5_for_m4k1ng_a_ch1ld_h4ppy_th1s_Chr1stma5}
