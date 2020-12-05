# O(nlogn)
# n = number of lines in file

def translateBinary(text, character):
	minVal = 0
	maxVal = 2**len(text) - 1
	for c in text:
		if c == character:
			maxVal = (minVal + maxVal) // 2
		else:
			minVal = ((minVal + maxVal) // 2) + 1
	return minVal

file = open("boardingPasses.txt", "r")
IDs = []
for line in file:
	row = translateBinary(line[:7], "F")
	col = translateBinary(line[-4:-1], "L")
	IDs.append(row*8 + col)
IDs.sort()
for x in range(len(IDs)-1):
	if IDs[x+1]-IDs[x] == 2:
		print(IDs[x]+1)
		break