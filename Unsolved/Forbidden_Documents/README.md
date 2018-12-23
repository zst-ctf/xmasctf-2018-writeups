# Forbidden Documents
Pwn

## Challenge 

	Hey. I discovered a service that provides access to the North Pole's archives, but the naughty list is somehow protected. Could you help me get that document?

	Server: nc 199.247.6.180 10004

	Author: littlewho

## Solution

	$ nc 199.247.6.180 10004
	Welcome to the Santa's Archive
	Name a document to open: flag
	flag
	This is a secret document!

From other challenges, usually there is a `redir.sh` file together with the `flag` file..

	$ nc 199.247.6.180 10004
	Welcome to the Santa's Archive
	Name a document to open: redir.sh
	redir.sh
	Do you want to read from other offset than 0? (y/n) 
	n
	How much should we read: 1000
	1000
	Content: #! /bin/bash
	cd /home/ctf
	sudo -u ctf socat tcp-l:10004,reuseaddr,fork exec:./random_exe_name,pty

We can try to extract ./random_exe_name

	
	$ strings -a -t x out_file
	43ae .init_array
	43ba .fini_array
	43c6 .dynamic
	43cf .got
	43d4 .got.plt
	43dd .data
	43e3 .bss
	43e8 .comment
	43f1 .gnu.build.attributes
	5042 X 5o
	5072 P 5o
	50b2 h 5o
	50e2 P 5o
	50fa H 5o

Binary roughly around 0x5042 bytes = 20546 bytes




	# readelf -h out_file1
	ELF Header:
	  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00 
	  Class:                             ELF64
	  Data:                              2's complement, little endian
	  Version:                           1 (current)
	  OS/ABI:                            UNIX - System V
	  ABI Version:                       0
	  Type:                              EXEC (Executable file)
	  Machine:                           Advanced Micro Devices X86-64
	  Version:                           0x1
	  Entry point address:               0x401130
	  Start of program headers:          64 (bytes into file)
	  Start of section headers:          17408 (bytes into file)
	  Flags:                             0x0
	  Size of this header:               64 (bytes)
	  Size of program headers:           56 (bytes)
	  Number of program headers:         11
	  Size of section headers:           64 (bytes)
	  Number of section headers:         30
	  Section header string table index: 29

https://stackoverflow.com/questions/2995347/how-can-i-find-the-size-of-a-elf-file-image-with-header-information

	
	Start of section headers = 17408 bytes
	Size of section headers = 64 (bytes)
	Number of section headers = 30

	Hence, file size = 17408 + 64*30 = 19328 bytes

dd if=out_file1 of=fixed bs=19328 count=1


## Flag

	??