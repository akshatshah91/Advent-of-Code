def flipX(tile):
	newTile = []
	for x in range(len(tile)-1, -1, -1):
		newTile.append(tile[x])
	return newTile

def flipY(tile):
	newTile = []
	for line in tile:
		line.reverse()
		newTile.append(line)
	return newTile

def rotate(tile):
	newTile = []
	for y in range(len(tile[0])):
		newLine = []
		for x in range(len(tile)):
			newLine.append(tile[x][y])
		newTile.append(newLine)
	return newTile

def compareSides(tile1, tile2):
	left = True
	right = True
	top = True
	bottom = True
	for x in range(len(tile1)):
		if tile1[x][0] != tile2[x][-1]:
			left = False
		if tile1[x][-1] != tile2[x][0]:
			right = False
	for x in range(len(tile1[0])):
		if tile1[0][x] != tile2[-1][x]:
			top = False
		if tile1[-1][x] != tile2[0][x]:
			bottom = False
	return left or right or top or bottom

def compareFlips(tile1, tile2):
	regular = compareSides(tile1, tile2)
	tile2 = flipX(tile2)
	X = compareSides(tile1, tile2)
	tile2 = flipY(tile2)
	XY = compareSides(tile1, tile2)
	tile2 = flipX(tile2)
	Y = compareSides(tile1, tile2)
	return regular or X or Y or XY

def compare(tile1, tile2):
	regular = compareFlips(tile1, tile2)
	tile2 = rotate(tile2)
	rotated = compareFlips(tile1, tile2)
	return regular or rotated


file = open("tiles.txt", "r")
tiles = {}
tileId = []
tile = []
for line in file:
	if "Tile" in line:
		tileId.append(int(line[5:-2]))
	elif line == "\n":
		tiles[tileId[-1]] = [tile, 0]
		tile = []
	else:
		newLine = [c for c in line[:-1]]
		tile.append(newLine)
for x in range(len(tileId)):
	for y in range(x+1, len(tileId)):
		if compare(tiles[tileId[x]][0], tiles[tileId[y]][0]):
			tiles[tileId[x]][1] += 1
			tiles[tileId[y]][1] += 1
value = 1
for k in tiles.keys():
	if tiles[k][1] == 2:
		value *= k
print(value)