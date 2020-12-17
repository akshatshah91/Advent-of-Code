import re

def insertRange(ranges, low, high):
	for x in range(len(ranges)):
		a,b = ranges[x]
		if b <= low:
			continue
		elif high <= a:
			ranges.insert(0, (low, high))
		else:
			ranges[x] = (min(a,low), max(high,b))
		while x < len(ranges)-1 and ranges[x][1] + 1 >= ranges[x+1][0]:
			ranges[x] = (ranges[x][0], max(ranges[x][1], ranges[x+1][1]))
			ranges.pop(x+1)
		return ranges
	ranges.append((low,high))
	return ranges

def checkRanges(ranges, num):
	for a,b in ranges:
		if a <= num <= b:
			return True
	return False

file = open("tickets.txt", "r")
ranges = []
invalid = []
lines = file.readlines()
x = 0
while lines[x] != "\n":
	rule = re.split(": |-| or ", lines[x][:-1])
	ranges = insertRange(ranges, int(rule[1]), int(rule[2]))
	ranges = insertRange(ranges, int(rule[3]), int(rule[4]))
	x += 1
for y in range(x+5, len(lines)):
	numbers = lines[y][:-1].split(",")
	for n in numbers:
		if not checkRanges(ranges, int(n)):
			invalid.append(int(n))
print(sum(invalid))