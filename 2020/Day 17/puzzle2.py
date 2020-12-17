def countActive(cube, w, x, y, z):
	active = 0
	for a in range(w-1, w+2):
		if 0 <= a < len(cube):
			for b in range(x-1, x+2):
				if 0 <= b < len(cube[0]):
					for c in range(y-1, y+2):
						if 0 <= c < len(cube[0][0]):
							for d in range(z-1, z+2):
								if 0 <= d < len(cube[0][0][0]) and (a != w or b != x or c != y or d != z):
									active += cube[a][b][c][d] == "#"
	return active

file = open("cubes.txt", "r")
cycles = 6
hyperCube = []
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
hyperCube.append(cube)
for x in range(cycles):
	hyperCube.insert(0, [[["." for c in range(len(cube[0][0]))] for b in range(len(cube[0]))] for a in range(len(cube))])
	hyperCube.insert(len(hyperCube), [[["." for c in range(len(cube[0][0]))] for b in range(len(cube[0]))] for a in range(len(cube))])
active = 0
for x in range(cycles):
	active = 0
	newHyper = []
	for a in range(len(hyperCube)):
		newCube = []
		for b in range(len(hyperCube[0])):
			newLayer= []
			for c in range(len(hyperCube[0][0])):
				newLine = []
				for d in range(len(hyperCube[0][0][0])):
					if hyperCube[a][b][c][d] == "." and countActive(hyperCube, a, b, c, d) == 3:
						newLine.append("#")
						active += 1
					elif hyperCube[a][b][c][d] == "#" and 2 <= countActive(hyperCube, a, b, c, d) <= 3:
						newLine.append("#")
						active += 1
					else:
						newLine.append(".")
				newLayer.append(newLine)
			newCube.append(newLayer)
		newHyper.append(newCube)
	hyperCube = newHyper
print(active)