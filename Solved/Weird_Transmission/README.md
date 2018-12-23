# Weird Transmission
Misc

## Challenge 

	We have intercepted a weird transmission coming from an unidentified radio station from the North Pole. Please decode it for us, it seems important.

	transmission.mp3

	Author: PinkiePie1189

## Solution

### 1. Reversed MP3

First we are given an MP3, which I suspected was reversed. I un-reversed it and I hear a message telling us a lot of information of large numbers.

> https://www.mp3-reverser.com/en/

### 2. Transcribe the Text

Next, the information contains a long string of numbers, hence I use an online speech-to-text service to help me.

> IBM Watson Speech to Text service:
> https://speech-to-text-demo.ng.bluemix.net/

This gives the following text.

> [Raw Text Here](./text_raw.txt)

From here, I need to fix a few text detection errors. It was mainly because of names for the large numbers being unrecognised and some other slurring

> Refer to: https://en.wikipedia.org/wiki/Names_of_large_numbers

After fixing all the errors, I have this set of text...

> [Final Text Here](./text_final.txt)

### 3. Convert English numbers into numerals

To convert to numbers, I modified [this script](http://code.activestate.com/recipes/550818-words-to-numbers-english/) to allow for huge number conversion.

> [My Converter (Python 3)](./converter.py)

Hence we have the following

	First coordinate:
	511716656388765455430016138955706839007890052532,
	1622805609316535864254436412730925222158623332074

	Second coordinate:
	390390142500834541752332649936545354218395003257,
	176460719206642987153469086794475382972064519404

	Third coordinate:
	608097554835704767294367078594102923662585120876,
	195121033653477539025103641752423493583135321761

	Santa's home will be located where the shape formed by
	these three points is in complete equilibrium

### 4. Find the equilibrium point

From the coordinates, it appears to be a triangle shape.

When it is said by equilibrium point, I assume it is the center of the triangle.

ie. [The centroid of the triangle](https://www.mathwarehouse.com/geometry/triangles/triangle-concurrency-points/centroid-of-triangle.php)

Simple math... Simply [get the average of the 3 points](https://www.basic-mathematics.com/centroid-of-a-triangle.html).

	>>> x1 = 511716656388765455430016138955706839007890052532
	>>> y1 = 1622805609316535864254436412730925222158623332074
	>>> x2 = 390390142500834541752332649936545354218395003257
	>>> y2 = 176460719206642987153469086794475382972064519404
	>>> x3 = 608097554835704767294367078594102923662585120876
	>>> y3 = 195121033653477539025103641752423493583135321761
	
	# Centroid of triangle
	>>> (x1+x2+x3) // 3
	503401451241768254825571955828785038962956725555
	
	>>> (y1+y2+y3) // 3
	664795787392218796811003047092608032904607724413

	# Ensure it is a perfect division with no remainder
	>>> ( (x1+x2+x3) // 3) * 3 == (x1+x2+x3)
	True
	>>> ( (y1+y2+y3) // 3) * 3 == (y1+y2+y3)
	True

With this we have 

	x0 = 503401451241768254825571955828785038962956725555
	y0 = 664795787392218796811003047092608032904607724413
	
Let's see if they mean anything in hex...

	>>> bytes.fromhex(hex(x0)[2:])
	b'X-MAS{An4ly71c_G30m3'
	>>> bytes.fromhex(hex(y0)[2:])
	b'try_S4v3d_Chr157m4s}'


## Flag

	X-MAS{An4ly71c_G30m3try_S4v3d_Chr157m4s}
