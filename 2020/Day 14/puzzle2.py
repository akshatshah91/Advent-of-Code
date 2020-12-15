import re

def allAddress(address, index):
	while index < len(address) and address[index] != "X":
		index += 1
	if index >= len(address):
		return [address]
	address1 = address.copy()
	address1[index] = "0"
	possible1 = allAddress(address1, index+1)
	address2 = address.copy()
	address2[index] = "1"
	possible2 = allAddress(address2, index+1)
	return possible1+possible2

file = open("initialization.txt", "r")
mask = None
memory = {}
for line in file:
	lineSplit = re.split("\[|\] = | = ", line[:-1])
	if lineSplit[0] == "mask":
		mask = lineSplit[1]
	else:
		address = list(f'{int(lineSplit[1]):036b}')
		for x in range(36):
			if mask[x] != "0":
				address[x] = mask[x]
		allAddresses = allAddress(address, 0)
		for x in allAddresses:
			memory["".join(x)] = int(lineSplit[2])
print(sum([memory[k] for k in memory.keys()]))
		