# Santa's Security Levels
Forensics

## Challenge 

	Santa has a flag hidden for you! Find out where. All letters, except for the X-MAS header, are lowercase.

	(Flag is Non-Standard, please add X-MAS{ } to the found string)

	Author: Googal

message.mp3

## Solution

There is morse code in the audio file.

I opened it in audacity and wrote down the code

	--. .. - .... ..- -...
	-.-. --- --
	--. --- --- --- --. .- .-..
	-..- -- .- ...

Now, use any morse code translator and get the following text

	github com gooogal xmas

Now we visit the page ("find out where")

https://github.com/Gooogal/xmas

And we get the message 
https://raw.githubusercontent.com/Gooogal/xmas/master/special%20message.txt

	vF ur uNq nAlguvat pbasvqraGvNy gb fnl, ur jebgr Vg ia pvcure, gung vF, ol FB punaTvat gur beqre bs gur Yrggref bs gur nycuNorg, gung abg n jbeQ pbhyq or ZnQR bHg.

It is a ceasar cipher. https://planetcalc.com/1434/

	iS he hAd aNything confidenTiAl to say, he wrote It vn cipher, that iS, by SO chanGing the order of the Letters of the alphAbet, that not a worD could be MaDE oUt.

Extract all capital letters

	SANTAISSOGLADMDEU


## Flag

	X-MAS{santaissogladmdeu}
