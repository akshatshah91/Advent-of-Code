# O(n)
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
highestID = 0
for line in file:
	row = translateBinary(line[:7], "F")
	col = translateBinary(line[-4:-1], "L")
	highestID = max(highestID, row*8 + col)
print(highestID)
