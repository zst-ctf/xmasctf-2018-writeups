
if __name__ == '__main__':
	
	for i in range(6 + 1):
		for j in range(0x23 + 1):
			print(f"i={i}, j={j}")
			print(f"lhs: str[{8*i}]")
			print(f"rhs: str[{8*((i<<2)+(i<<3)+j)}] == str[8*(({i<<2})+({i<<3})+{j})]")
			print()
            #str[8*i] += str[8*((i<<2)+(i<<3)+j)] * sub_400556(j, 0, 0)
