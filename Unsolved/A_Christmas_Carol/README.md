# A Christmas Carol
Reverse

## Challenge 

	Santa found an interesting machine that transforms text to beautiful Christmas carols. He also found a carol that contains a hidden message. Help Santa find out what the secret message is!

	Authors: littlewho + Gabies

	carol.zip

## Solution

We are given an `.exe` file.

One thing to note is that is does not run on Windows... In fact, it is a linux executable.
	
	$ file encoder.exe 
	encoder.exe: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=f51f0d393d69dc03ad75319591f25174696c6ac0, stripped

It runs well on Ubuntu after installing some dependencies

	# ./encoder.exe 
	Traceback (most recent call last):
	  File "/home/littlewho/our_ctf/midi/chall.py", line 1, in <module>
	ImportError: No module named midi

	# pip install python-midi

	Successfully installed python-midi-0.2.4
	
	# ./encoder.exe 
	Usage: ./exe <infile> <outfile>


Now we know it is a python program packaged in a linux executable.

	$ strings encoder.exe | head
	/lib64/ld-linux-x86-64.so.2
	Qtilj
	JbX0
	x[B\
	5z)V]
	TGt<
	libpython2.7.so.1.0
	__gmon_start__
	PyExc_OverflowError
	Py_InteractiveFlag

There is no way to decompile and get back the Python script.

In one part of the strings, we see that it is [compiled with Nuitka](http://nuitka.net/pages/overview.html).

	_nuitka_compiled_modules_loader
	Setup nuitka compiled module/bytecode/shlib importer.




Since this is an exe, let's move to a Windows machine.

https://hshrzd.wordpress.com/2018/01/26/solving-a-pyinstaller-compiled-crackme/
https://stackoverflow.com/questions/44799687/unpacking-pyinstaller-packed-files


https://pyinstaller.readthedocs.io/en/v3.3.1/advanced-topics.html
https://stackoverflow.com/questions/44799687/unpacking-pyinstaller-packed-files

## Flag

	??