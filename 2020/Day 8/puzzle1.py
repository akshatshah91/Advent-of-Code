file = open("instructions.txt")
lines = file.readlines()
indexes = []
lineIndex = 0
accumulator = 0
while lineIndex not in indexes:
	indexes.append(lineIndex)
	instruction,num = lines[lineIndex].split()
	if instruction == "acc":
		accumulator += int(num)
		lineIndex += 1
	elif instruction == "jmp":
		lineIndex += int(num)
	else:
		lineIndex += 1
print(accumulator)