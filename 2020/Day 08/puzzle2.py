def run(lines, indexes, lineIndex):
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
		if lineIndex == len(lines):
			return True,accumulator
	return False,accumulator

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
		works,a = run(lines, indexes.copy(), lineIndex+1)
		if works:
			accumulator += a
			break
		lineIndex += int(num)
	else:
		works,a = run(lines, indexes.copy(), lineIndex+int(num))
		if works:
			accumulator += a
			break
		lineIndex += 1
print(accumulator)