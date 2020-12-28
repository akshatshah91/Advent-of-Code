def checkDest(cups, current, dest):
	newCurrent = current
	for _ in range(3):
		if dest == cups[current]:
			return False
		current = cups[current]
	return True

puzzleInput = "942387615"
cups = [None] * 1000001
for x in range(len(puzzleInput)-1):
	cups[int(puzzleInput[x])] = int(puzzleInput[x+1])
val = len(puzzleInput)+1
index = int(puzzleInput[-1])
while val <= 1000000:
	cups[index] = val
	index = val
	val += 1
cups[-1] = int(puzzleInput[0])
current = int(puzzleInput[0])
for _ in range(10000000):
	dest = current
	while True:
		dest -= 1
		if dest == 0:
			dest = len(cups)-1
		if checkDest(cups, current, dest):
			break
	afterDest = cups[dest]
	afterPick = cups[cups[cups[cups[current]]]]
	cups[dest] = cups[current]
	cups[current] = afterPick
	cups[cups[cups[cups[dest]]]] = afterDest
	current = cups[current]
num1 = cups[1]
num2 = cups[num1]
print(num1*num2)
