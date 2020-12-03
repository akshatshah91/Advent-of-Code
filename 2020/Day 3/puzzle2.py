# O(n)
# n = number of lines in file

file = open("map.txt", "r")
multiple = 1
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
map = []
for line in file:
	map.append(line[:-1])
for x,y in slopes:
	xIndex = 0
	yIndex = 0
	trees = 0
	while yIndex < len(map):
		trees += map[yIndex][xIndex] == '#'
		xIndex = (xIndex + x) % len(map[0])
		yIndex += y
	multiple *= trees
print(multiple)