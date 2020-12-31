file = open("instructions.txt", "r")
line = file.readline()
floor = 0
for c in line:
	if c == "(":
		floor += 1
	elif c == ")":
		floor -= 1
print(floor)