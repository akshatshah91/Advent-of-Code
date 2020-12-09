file = open("data.txt", "r")
numbers = []
invalid = None
for line in file:
	if invalid == None and len(numbers) >= 25:
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
			invalid = int(line)
	numbers.append(int(line))
l = 0
r = 2
while r <= len(numbers):
	total = sum(numbers[l:r])
	if total == invalid:
		print(min(numbers[l:r])+max(numbers[l:r]))
		break
	elif total < invalid:
		r += 1
	else:
		l += 1