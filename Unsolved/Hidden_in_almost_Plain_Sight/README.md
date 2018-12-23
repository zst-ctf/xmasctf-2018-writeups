# Hidden in almost Plain Sight
Forensics

## Challenge 

	A strange file was sent to Santa's email address and he is puzzled. Help him find what's wrong with the file and you can keep any flag you find in the process.

	Author: Googal
	Celebration

## Solution

	$ xxd Celebration | head
	00000000: 8900 0047 0d0a 1a0a 0000 000d 4948 4452  ...G........IHDR
	00000010: 0000 15f0 0000 0cb2 0802 0000 00eb a6d7  ................
	00000020: 5f00 0000 0970 4859 7300 000e f300 000e  _....pHYs.......
	00000030: f301 1c53 993a 0000 0011 7445 5874 5469  ...S.:....tEXtTi
	00000040: 746c 6500 5044 4620 4372 6561 746f 7241  tle.PDF CreatorA
	00000050: 5ebc 2800 0000 1374 4558 7441 7574 686f  ^.(....tEXtAutho
	00000060: 7200 5044 4620 546f 6f6c 7320 4147 1bcf  r.PDF Tools AG..
	00000070: 7730 0000 002d 7a54 5874 4465 7363 7269  w0...-zTXtDescri
	00000080: 7074 696f 6e00 0008 99cb 2829 29b0 d2d7  ption.....())...
	00000090: 2f2f 2fd7 2b48 49d3 2dc9 cfcf 29d6 4bce  ///.+HI.-...).K.

We see IHDR in the header, which means this is a corrupted PNG file.

After fixing, we see an image with a blanked out region in Pink...

Use Zsteg, we realise there is some additional data

	$ zsteg Fixed.png
	extradata:imagedata .. 
	    00000000: 04 f8 f7 f4 02 04 05 04  04 04 02 02 04 fe 01 fe  |................|
	    00000010: 01 00 02 02 01 01 02 01  01 fd fe fc 00 fe 00 ff  |................|
	    00000020: 00 fe fe ff fe fb f9 f7  f0 f0 ee fa f9 f8 05 05  |................|
	    00000030: 03 0a 04 0e 03 06 05 03  05 04 ff 01 00 ff 01 01  |................|
	    00000040: 02 03 00 04 04 04 01 01  ff 02 03 06 00 00 ff 01  |................|
	    00000050: ff fe fd fe ff 00 fe fe  ff ff ff 02 03 01 03 02  |................|
	    00000060: 03 ff 00 00 00 ff 00 01  01 01 fe 00 01 01 00 00  |................|
	    00000070: 00 00 00 01 01 01 02 01  02 fe 01 00 00 00 01 02  |................|
	    00000080: 00 01 fe 01 00 02 01 01  01 01 01 ff 00 ff 00 00  |................|
	    00000090: 00 00 fe ff 00 01 00 ff  02 01 00 fe fe 00 00 00  |................|
	    000000a0: 01 00 00 ff 00 00 ff ff  ff 00 00 00 fe ff ff ff  |................|
	    000000b0: ff fd fe fe 00 00 00 00  01 01 01 01 01 01 00 ff  |................|
	    000000c0: 01 01 00 fe 02 01 ff ff  00 ff 00 01 00 00 01 ff  |................|
	    000000d0: 02 01 fd ff ff 01 00 ff  00 fe fe fe ff ff fd ff  |................|
	    000000e0: fe fe ff ff ff fc fe ff  fe fe fe fe fe fe 00 fe  |................|
	    000000f0: ff 01 06 04 00 00 00 ff  fe 01 00 02 01 03 03 03  |................|
	meta Title          .. text: "PDF Creator"
	meta Author         .. text: "PDF Tools AG"
	meta Description    .. text: "http://www.pdf-tools.com"
	imagedata           .. text: ".3-bca#&"
	b1,r,msb,xy         .. text: "?]wur ^'"
	b1,b,lsb,xy         .. text: "nP~8R}wW"
	b3,bgr,msb,xy       .. text: "^R%[$>c9"





https://www.pdf-tools.com/pdf20/en/products/pdf-converter-validation/image-to-pdf-converter/
Test Online

https://www.pdf-online.com/osa/img2pdf.aspx

## Flag

	??