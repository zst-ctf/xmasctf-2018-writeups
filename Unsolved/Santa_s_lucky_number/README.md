# Santa's lucky number
Web

## Challenge 

	Come on! Santa's lucky number is pretty predictable, don't you think? ;)

	Server: http://199.247.6.180:12005

	Author: Vlad

## Solution

I didn't solve this during the CTF, and I did a bruteforce until 1000 with no luck.

I got confused when the page param allows for non-digits

	http://199.247.6.180:12005/?page=Array
	9aac6c709ef2bc1612339bd89b1f676344e5c05952a0bc14d0c3e4512628c91cc011095de18faa0f9f9039a943b8bedf87da4417c7a36fbc4fa06a119e6e5588

	http://199.247.6.180:12005/?page[]=123
	9aac6c709ef2bc1612339bd89b1f676344e5c05952a0bc14d0c3e4512628c91cc011095de18faa0f9f9039a943b8bedf87da4417c7a36fbc4fa06a119e6e5588

---

From reading other people's writeups, solution was simply to continue bruteforce until around 1327.

## Flag

	??