# Endless Christmas
Reverse

## Challenge 

	This Christmas seems that it will never end...

	Authors: littlewho + Gabies

	 chall

## Solution

Running ./chall yields some more binaries

And then running those will yield another set of binaries.


In particular, I did this sequence

	./chall
	./file26WiYI
	./fileWbDX36

Then I decompiled `fileWbDX36` in hopper.

	int main() {
	    var_11 = 0x1;
	    printf("Enter the flag: ");
	    __isoc99_scanf(0x400721, 0x6010c0);
	    var_18 = 0x0;
	    goto loc_400648;

	loc_400648:
	    if (sign_extend_64(var_18) < strlen("U @L^vi>n=i>R9;9<cR9ciR9;9<cR9ciR9;9<cR9ciR9;9<cR9ciRka9;p")) goto loc_40061f;

	loc_40065d:
	    if (var_11 != 0x0) {
	            puts("MERRY CHRISTMAS!");
	    }
	    else {
	            puts(0x400735);
	    }
	    return 0x0;

	loc_40061f:
	    if ((*(int8_t *)(sign_extend_32(var_18) + 0x6010c0) & 0xff) == (*(int8_t *)(sign_extend_32(var_18) + "U @L^vi>n=i>R9;9<cR9ciR9;9<cR9ciR9;9<cR9ciR9;9<cR9ciRka9;p") & 0xff ^ 0xd)) goto loc_400644;

	loc_40063e:
	    var_11 = 0x0;
	    goto loc_40065d;

	loc_400644:
	    var_18 = var_18 + 0x1;
	    goto loc_400648;
	}

From this, we see at `loc_40061f`, that the string has an XOR-key of 0x0d. Decoding it gets us the flag...


	$ python3
	>>> txt = bytes(b'U @L^vi>n=i>R9;9<cR9ciR9;9<cR9ciR9;9<cR9ciR9;9<cR9ciRka9;p')
	>>> for t in txt: print(chr(t^0xd), end='')
	... 
	X-MAS{d3c0d3_4641n_4nd_4641n_4nd_4641n_4nd_4641n_4nd_fl46}


## Flag

	X-MAS{d3c0d3_4641n_4nd_4641n_4nd_4641n_4nd_4641n_4nd_fl46}
