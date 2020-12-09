# O(n * k)
# n = number of lines in file
# k = number of characters in line

file = open("answers.txt", "r")
count = 0
answerDict = {}
for line in file:
	if line == "\n":
		count += len(answerDict.keys())
		answerDict = {}
	for c in line[:-1]:
		answerDict[c] = 1
count += len(answerDict.keys())
print(count)
