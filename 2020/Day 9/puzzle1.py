file = open("data.txt", "r")
numbers = []
for line in file:
	if len(numbers) >= 25:
		numSub = numbers[-25:].copy()
		numSub.sort()
		l = 0
		r = 24
		while l < r:
			if numSub[l]+numSub[r] == int(line):
				break
			elif numSub[l]+numSub[r] < int(line):
				l += 1
			else:
				r -= 1
		if l >= r:
			print(int(line))
			break
	numbers.append(int(line))