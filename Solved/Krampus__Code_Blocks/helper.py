

def krampus_string(s):
	out = []
	for ch in list(s):
		ch = ord(ch)
		out.append(f"chr({ch})")
	return '+'.join(out)

