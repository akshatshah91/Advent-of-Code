import copy

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
		for x in range(len(tile)-1, -1, -1):
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
	return [left,right,top,bottom]

def compareFlips(tile1, tile2):
	regular = sum(compareSides(tile1, tile2))
	if regular:
		return True,tile2
	tile2 = flipX(tile2)
	X = sum(compareSides(tile1, tile2))
	if X:
		return True,tile2
	tile2 = flipY(tile2)
	XY = sum(compareSides(tile1, tile2))
	if XY:
		return True,tile2
	tile2 = flipX(tile2)
	Y = sum(compareSides(tile1, tile2))
	return Y,tile2

def compare(tile1, tile2):
	regular,correct2 = compareFlips(tile1, tile2)
	if regular:
		return True,correct2
	tile2 = rotate(tile2)
	rotated,correct2 = compareFlips(tile1, tile2)
	return rotated,correct2

def checkRight(tile1, tile2):
	for x in range(len(tile1)):
		if tile1[x][-1] != tile2[x][0]:
			return False
	return True

def checkDown(tile1, tile2):
	for x in range(len(tile1[0])):
		if tile1[-1][x] != tile2[0][x]:
			return False
	return True

def find(fullImage, monster):
	count = 0
	for x in range(len(fullImage)-len(monster)):
		for y in range(len(fullImage[x]) - len(monster[0])):
			match = True
			for a in range(len(monster)):
				for b in range(len(monster[0])):
					if monster[a][b] == "#" and fullImage[a+x][b+y] != "#":
						match = False
			if match:
				count += 1
				for a in range(len(monster)):
					for b in range(len(monster[0])):
						if monster[a][b] == "#":
							fullImage[a+x][b+y] = "O"
	return count,fullImage

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
tileQueue = [tileId[0]]
while len(tileId) > 0:
	tileId.remove(tileQueue[0])
	for t in tileId:
		match,newTile = compare(tiles[tileQueue[0]][0], copy.deepcopy(tiles[t][0]))
		if match:
			tiles[tileQueue[0]][1] += 1
			tiles[tileQueue[0]].append(t)
			tiles[t][0] = newTile
			tiles[t][1] += 1
			tiles[t].append(tileQueue[0])
			if t not in tileQueue:
				tileQueue.append(t)
	tileQueue.pop(0)
left = None
for k in tiles.keys():
	if tiles[k][1] == 2:
		right = False
		down = False
		for x in range(2, len(tiles[k])):
			val = compareSides(tiles[k][0], tiles[tiles[k][x]][0])
			if val[1]:
				right = True
			elif val[3]:
				down = True
		if right and down:
			left = k
image = [[tiles[left][0]]]
last = False
while True:
	current = left
	while True:
		noneRight = True
		for x in tiles[current][2:]:
			if checkRight(tiles[current][0], tiles[x][0]):
				tiles[current].remove(x)
				current = x
				image[-1].append(tiles[current][0])
				noneRight = False
				break
		if noneRight:
			break
	for x in tiles[left][2:]:
		if checkDown(tiles[left][0], tiles[x][0]):
			tiles[left].remove(x)
			left = x
			image.append([tiles[left][0]])
			break
	if last:
		break
	elif tiles[left][1] == 2:
		last = True
fullImage = []
index = 0
for x in range(len(image)):
	for a in range(8):
		fullImage.append([])
	for y in range(len(image[x])):
		for a in range(1, len(image[x][y])-1):
			fullImage[index+a-1] += image[x][y][a][1:-1]
		image[x][y] = image[x][y][1:-1]
	index += 8
monster = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]
for x in range(2):
	for y in range(4):
		count,newImage = find(fullImage, monster)
		if count != 0:
			roughness = 0
			for a in newImage:
				for b in a:
					roughness += b == "#"
			print(roughness)
			break
		fullImage = rotate(fullImage)
	fullImage = flipX(fullImage)