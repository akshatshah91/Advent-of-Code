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

def sweep(possible):
	for k in possible.keys():
		if len(possible[k]) == 1:
			for i in possible.keys():
				if k != i and possible[k][0] in possible[i]:
					possible[i].remove(possible[k][0])
	return possible

file = open("tickets.txt", "r")
ranges = []
rules = {}
possible = {}
lines = file.readlines()
x = 0
while lines[x] != "\n":
	rule = re.split(": |-| or ", lines[x][:-1])
	rules[rule[0]] = [(int(rule[1]), int(rule[2])), (int(rule[3]), int(rule[4]))]
	ranges = insertRange(ranges, int(rule[1]), int(rule[2]))
	ranges = insertRange(ranges, int(rule[3]), int(rule[4]))
	x += 1
myTicket = lines[x+2][:-1].split(",")
for k in rules.keys():
	possible[k] = [x for x in range(len(myTicket))]
for y in range(x+5, len(lines)):
	numbers = [int(n) for n in lines[y][:-1].split(",")]
	invalid = False
	for n in numbers:
		if not checkRanges(ranges, n):
			invalid = True
			break
	if not invalid:
		for z in range(len(numbers)):
			for k in rules.keys():
				if not checkRanges(rules[k], numbers[z]) and z in possible[k]:
					possible[k].remove(z)
for x in range(len(possible.keys())):
	possible = sweep(possible)
departure = 1
for k in possible.keys():
	if "departure" in k:
		departure *= int(myTicket[possible[k][0]])
print(departure)