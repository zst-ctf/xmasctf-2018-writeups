# Santa's No Password Login System
Web

## Challenge 

	We all know that Santa is quite an old man. He sometimes forgets things. Including his password.

	Therefore, our high-tech gnomegineer department worked the whole last night to develop a new login system, that requires no passwords! Nifty.

	Server: http://199.247.6.180:12003

	Author: Milkdrop

## Solution

The page:

	Santa's No-Password Login!

	You don't seem to be using an official Computer from Santa's Laboratory!

	Access Denied!

Try some headers

	curl -i -H "X-Originating-IP: 127.0.0.1" -H "X-Forwarded-For: 127.0.0.1" -H "X-Remote-IP: 127.0.0.1" -H "X-Remote-Addr: 127.0.0.1" http://199.247.6.180:12003/

	curl http://199.247.6.180:12003/ -H 'Host: Santa' -v

???

## Flag

	??