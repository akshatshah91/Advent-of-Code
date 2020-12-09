# O(n * k)
# n = number of lines in file
# k = number of characters in line

file = open("answers.txt", "r")
count = 0
answerDict = {}
people = 0
for line in file:
	if line == "\n":
		for k in answerDict.keys():
			count += answerDict[k] == people
		answerDict = {}
		people = 0
		continue
	for c in line[:-1]:
		if c in answerDict:
			answerDict[c] += 1
		else:
			answerDict[c] = 1
	people += 1
for k in answerDict.keys():
	count += answerDict[k] == people
print(count)
