file = open("instructions.txt", "r")
line = file.readline()
floor = 0
for x in range(len(line)):
	if line[x] == "(":
		floor += 1
	elif line[x] == ")":
		floor -= 1
	if floor == -1:
		print(x+1)
		break