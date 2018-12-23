# CatanaGift
Reverse

## Challenge 

	Something curious happened... a weird guy named Catana has created a secret message printer that uses a very complex algorithm. You and Santa's MechaGnomes have to put your great minds togheter and get the program to print the message a bit faster.

	Authors: littlewho + Gabies

	catana

## Solution


	int sub_400556(int arg0, int arg1, int arg2) {
	    //var_14 = arg0;
	    //var_18 = arg1;
	    //var_1C = arg2;
	    if ((arg1 == arg0) && (arg2 == arg0)) {
            return 0x1;
	    } else {
	    	int var_8 = 0x0;
            if (arg1 < arg0) {
                var_8 = sub_400556(arg0, arg1 + 0x1, arg2);
            }
            if ((arg2 < arg0) && (arg2 < arg1)) {
                var_8 += sub_400556(arg0, arg1, arg2 + 0x1);
            }
            return var_8;
	    }
	    return 0;
	}

	int sub_4005d6() {
		str = &0x601860;

	    for (i = 0x0; i <= 0x6; i++) {
	            for (j = 0x0; j <= 0x23; j++) {
	            	str[8*i] += str[8*((i<<2)+(i<<3)+j)] * sub_400556(j, 0, 0)
	            }
	    }
	    for (var_1C = 0x0; var_1C <= 0x6; var_1C = var_1C + 0x1) {
	            var_20 = 0x0;
	            memset(&var_2C, 0x0, 0x8);
	            while (*(sign_extend_32(var_1C) * 0x8 + str) != 0x0) {
	                    rdx = *(sign_extend_32(var_1C) * 0x8 + str) & 0x8000000000000000 ? 0xffffffffffffffff : 0x0;
	                    rax = var_20;
	                    var_20 = rax + 0x1;
	                    *(int8_t *)(rbp + sign_extend_32(rax) + 0xffffffffffffffd4) = (*(sign_extend_32(var_1C) * 0x8 + str) + (rdx >> 0x38) & 0xff) - (rdx >> 0x38);
	                    rax = *(sign_extend_32(var_1C) * 0x8 + str);
	                    rdx = rax + 0xff;
	                    if (rax < 0x0) {
	                            rax = rdx;
	                    }
	                    *(sign_extend_32(var_1C) * 0x8 + str) = SAR(rax, 0x8);
	            }
	            for (var_24 = var_20 - 0x1; var_24 >= 0x0; var_24 = var_24 - 0x1) {
	                    putchar((*(int8_t *)(rbp + (var_24) + 0xffffffffffffffd4) & 0xff));
	            }
	    }
	    putchar(0xa);
	    return 0x0;
	}


It is seen that this function returns a [sequence called the Catalan number](https://en.wikipedia.org/wiki/Catalan_number)...

	sub_400556(x, 0, 0);
	f(1) = 1
	f(2) = 2
	f(3) = 5
	f(4) = 14
	f(5) = 42
	f(6) = 132



	(gdb) br *0x4005d6
	Breakpoint 1 at 0x4005d6
	(gdb) run
	Starting program: /FILES/catana 

	Breakpoint 1, 0x00000000004005d6 in ?? ()
	(gdb) disas 0x4005d6           
	No function contains specified address.
	(gdb) disas 0x4005d6, 0x4006d6

	(gdb) set {unsigned char} 0x000000000040062d = 0x90
	(gdb) set {unsigned char} 0x000000000040062e = 0x90
	(gdb) set {unsigned char} 0x000000000040062f = 0x90
	(gdb) set {unsigned char} 0x0000000000400630 = 0x90
	(gdb) set {unsigned char} 0x0000000000400631 = 0x90



## Flag

	??