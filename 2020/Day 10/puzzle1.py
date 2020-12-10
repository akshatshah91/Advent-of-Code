file = open("adapters.txt", "r")
adapters = [int(line) for line in file]
adapters.append(0)
adapters.sort()
diffDict = {1:0, 2:0, 3:1}
for x in range(len(adapters)-1):
	diffDict[adapters[x+1]-adapters[x]] += 1
print(diffDict[1]*diffDict[3])