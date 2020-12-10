file = open("adapters.txt", "r")
adapters = [int(line) for line in file]
adapters.append(0)
adapters.sort()
possibilitiesDict = {0:1}
for x in range(1, len(adapters)):
	possibilities = 0
	for y in range(x-3, x):
		if y < 0:
			continue
		elif adapters[x]-adapters[y] <= 3:
			possibilities += possibilitiesDict[adapters[y]]
	possibilitiesDict[adapters[x]] = possibilities
print(possibilitiesDict[max(adapters)])