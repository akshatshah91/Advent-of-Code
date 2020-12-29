def countBlack(grid, newGrid, x, y):
	black = 0
	surround = [(x-1,y), (x-1,y+1), (x,y+1), (x+1,y), (x+1,y-1), (x,y-1)]
	for loc in surround:
		if loc in grid and grid[loc] == 1:
			black += 1
		elif loc not in grid:
			newGrid[loc] = 0
	return black,newGrid

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
newGrid = {}
for (x,y) in grid.keys():
	_,newGrid = countBlack(grid,newGrid,x,y) # used to just add all the white spaces to the grid
	newGrid[(x,y)] = grid[(x,y)]
grid = newGrid
for a in range(100):
	newGrid = {}
	for (x,y) in grid.keys():
		black,newGrid = countBlack(grid,newGrid,x,y)
		if grid[(x,y)] == 1 and (black == 0 or black > 2):
			newGrid[(x,y)] = 0
		elif grid[(x,y)] == 0 and black == 2:
			newGrid[(x,y)] = 1
		else:
			newGrid[(x,y)] = grid[(x,y)]
	grid = newGrid
black = 0
for k in grid.keys():
	black += grid[k] == 1
print(black)