file = open("directions.txt", "r")
grid = {}
for line in file:
	x = 0
	y = 0
	a = 0
	while a < len(line):
		if line[a] == "e":
			x += 1
		elif line[a] == "w":
			x -= 1
		elif line[a] == "n":
			y += 1
			if line[a+1] == "w":
				x -= 1
			a += 1
		elif line[a] == "s":
			y -= 1
			if line[a+1] == "e":
				x += 1
			a += 1
		a += 1
	if (x,y) in grid:
		grid[(x,y)] = grid[(x,y)]^1
	else:
		grid[(x,y)] = 1
black = 0
for k in grid.keys():
	black += grid[k] == 1
print(black)