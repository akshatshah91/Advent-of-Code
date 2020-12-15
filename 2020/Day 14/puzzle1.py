import re

file = open("initialization.txt", "r")
mask = None
memory = {}
for line in file:
	lineSplit = re.split("\[|\] = | = ", line[:-1])
	if lineSplit[0] == "mask":
		mask = lineSplit[1]
	else:
		num = list(f'{int(lineSplit[2]):036b}')
		for x in range(36):
			if mask[x] != "X":
				num[x] = mask[x]
		memory[int(lineSplit[1])] = int("".join(num), 2)
print(sum([memory[k] for k in memory.keys()]))
