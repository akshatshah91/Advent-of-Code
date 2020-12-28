puzzleInput = "942387615"
cups = [int(n) for n in puzzleInput]
current = 0
for x in range(100):
	pick = []
	for _ in range(3):
		if current+1 >= len(cups):
			pick.append(cups.pop(0))
			current -= 1
		else:
			pick.append(cups.pop(current+1))
	destVal = cups[current]-1
	while destVal in pick:
		destVal -= 1
	if destVal == 0:
		destVal = max(cups)
	dest = cups.index(destVal)
	cups = cups[:(dest+1)] + pick + cups[(dest+1):]
	if dest < current:
		current += 3
	current = (current + 1) % len(cups)
one = cups.index(1)
print("".join([str(x) for x in cups[one+1:] + cups[:one]]))