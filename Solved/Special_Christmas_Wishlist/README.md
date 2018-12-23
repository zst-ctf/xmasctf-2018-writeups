# Special Christmas Wishlist
Crypto

## Challenge 

	While Santa was looking through the wishlists of the childern all around the world he came across a very strange looking one. Help Santa decode the letter in order to fulfill the wishes of this child.

	(Flag is Non-Standard)

	wishlist.png

	UPDATE: flag is lowercase!

	Author: Gabies

## Solution

### Concept

**Concept is to map each glyph/symbol to a latin alphabet. After that, input it into any substitution cipher solver such as quipqiup.com**

I've done simpler versions of this in PACTF/PicoCTF. However, we see that this time, it is a huge sample of text.

### Solving using OpenCV

Resources:
- https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html
- https://stackoverflow.com/questions/51091865/how-to-extract-these-6-symbols-signatures-from-paper-opencv
- http://blog.ayoungprogrammer.com/2013/01/equation-ocr-part-1-using-contours-to.html/

I decided to create a scanner in Python + OpenCV... And then we have the mapping in `output.txt` and `output.png`...

	python3 opencv.py 

But then we notice in `output.png`, that FA is considered as one character (somehow it was being detected as 2 chars). So remember to fix it before placing into substitution cipher solvers.

	FA -> F

### Results using quipqiup.com

Hence, we get this result in https://quipqiup.com/

	L?TITUDE LONGITUDE HOUSE S?GN GIR?FFE F?MILY BOOKENDS HTML BEER GLASSES SET OF TWO B?D DOG WISDOM TUMBLERS 
	ADVENTURER MULTITOOL CLIP W?TCH TW?G MARSHM?LLOW SKEWER NEST?NG STORAGE CONTAINERS SM?L?NG ?I1O GARDEN 
	SCULPTURE LONG D?ST?NCE TOUCH L?MP MULT?COLOR OMBRE STEMLESS WINE GL?SS SET ?PHONE CH?RGER STICKER FACES SET 
	PEDESTAL ?EWELRY HOLDER ARTIS?N?L B?MBOO SALT CHEST AUROR? SM?RT L?GHT?NG P?NELS THE SEA SERPENT G?RDEN 
	SCULPTURE THE 2U?TE AMA1?NG 2UEST FOR 2UER?ES RECYCLED GL?SS TREE GLOBES RELAT?ONSHIPS NEW YORK T?MES CUSTOM 
	FRONT P?GE PU11LE THE BEST SLING BEVERAGE COOLER TR?O M??ED METALS E?RR?NGS BIRTH MONTH FLOWER NECKLACE A 
	MOTHERS LOVE IS BEYOND ME?SURE SPOON SET WEDD?NG W?LT1 PERSONAL?1ED ?RT PERSONAL?1ED GOODN?GHT L?TTLE ME BOOK 
	CUSTOM PET NOSE PR?NT NECKL?CES CUSTOM PET P?LLOWS 2WERTY KEYBOARD LLAMARAMA L?RGE 1IPPER POUCH MIMOS? D??GRAM 
	GL?SSW?RE SET OF THREE THANK YOU FOR YOUR PART ?N MY ?OURNEY NECKL?CE YOG? POSE H?NG?NG SCULPTURES THE BIKE 
	CH??N BOWL CR?MSON HEART UMBRELL? THE 2U?1 INS?DE THE M?1E MENS HERB?L W?RM?NG SL?PPERS YOURS MINE ?ND OURS 
	ENGRAVED DECANTER SET THE ANNIVERSARY ?OURN?L MOMMA BIRD CUFF WINE BARREL GU?TAR RACK THE PLUSH ORG?NS G?RL?C 
	GR?TER AND OIL DIPP?NG DISH OKTOBERFEST ALE BEER BREWING K?T M?TES FOR LIFE BOOK LOVERS LIGHTWEIGHT SCARVES 
	CONSTITUTION OF UN?TED ST?TES OF ?MERIC? GL?SS GOLF GL?SSES PEWTER ANGEL CO?NS SET OF TWELVE BUNNY FELT BABY 
	SL?PPERS PERSONAL?1ED TREE TRUNK GLASSWARE DUO E?PECT?NG YOU A KEEPS?KE PREGNANCY ?OURNAL THE BERRY BUDDY THE 
	BIRD?E YARN BOWL K?NTH? CH?NDEL?ERS EARRINGS PERSONAL?1ED MY VERY OWN NAME BOOK UN?CORN AND R??NBOW MISMATCHED 
	EARRINGS SLOTH P?LS MOB?LE B?T ON ? BR?NCH PERSONAL?1ED CUTTING BO?RD SMOKE DETECTOR DE?CT?VAT?ON TOWEL THE 
	LUNE L?GHT PERSONAL?1ED ?NN?VERS?RY PUSHP?N US? MAP MENS TACO SOCKS ELWOOD THE UNICORN CERE?L BOWL ?NTERSECTION 
	OF LOVE PHOTO PRINT THE LITTLE PAT?ENT CIRCLE OF F?MILY ?ND FRIENDS SERVING BOWL GLASS FLOWER GARDEN 
	CENTERPIECE BIRTHSTONE M?NERAL SO?PS SET OF FOUR GOLF GL?SSES THE CED?R THUMB PIANOS CUSTOM MAP CO?STER SET BIG 
	PERSONAL?TY DESK S?GNS SEA STONE SPL?SH SPONGE HOLDER YOUR MOST DESIRED OB?ECT THIS CHRISMAS THE FLAG IS 
	?MASYOU?RESOGOODATSUBSTITUTIONCIPHERS

Last line gives us the flag

	THE FLAG IS ?MASYOU?RESOGOODATSUBSTITUTIONCIPHERS

And we can infer the missing alphabets

	XMASYOUARESOGOODATSUBSTITUTIONCIPHERS

## Flag

Flag is lowercase!

	xmasyouaresogoodatsubstitutionciphers
