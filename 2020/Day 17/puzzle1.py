def countActive(cube, x, y, z):
	active = 0
	for a in range(x-1, x+2):
		if 0 <= a < len(cube):
			for b in range(y-1, y+2):
				if 0 <= b < len(cube[0]):
					for c in range(z-1, z+2):
						if (a != x or b != y or c != z) and 0 <= c < len(cube[0][0]):
							active += cube[a][b][c] == "#"
	return active

file = open("test.txt", "r")
cycles = 6
cube = []
layer = []
for line in file:
	line = [c for c in line[:-1]]
	for x in range(cycles):
		line.insert(0, ".")
		line.insert(len(line), ".")
	layer.append(line)
for x in range(cycles):
	layer.insert(0, ["." for y in range(len(layer[0]))])
	layer.insert(len(layer), ["." for y in range(len(layer[0]))])
cube.append(layer)
for x in range(cycles):
	cube.insert(0, [["." for z in range(len(layer[0]))] for y in range(len(layer))])
	cube.insert(len(cube), [["." for z in range(len(layer[0]))] for y in range(len(layer))])
active = 0
for x in range(0,cycles):
	active = 0
	newCube = []
	for a in range(len(cube)):
		newLayer = []
		for b in range(len(cube[0])):
			newLine = []
			for c in range(len(cube[0][0])):
				if cube[a][b][c] == "." and countActive(cube, a, b, c) == 3:
					newLine.append("#")
					active += 1
				elif cube[a][b][c] == "#" and 2 <= countActive(cube, a, b, c) <= 3:
					newLine.append("#")
					active += 1
				else:
					newLine.append(".")
			newLayer.append(newLine)
		newCube.append(newLayer)
	cube = newCube
print(active)