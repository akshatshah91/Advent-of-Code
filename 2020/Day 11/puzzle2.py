def countDirection(seats, x, y, a, b):
	newX = x+a
	newY = y+b
	while 0 <= newX < len(seats) and 0 <= newY < len(seats[x]):
		if seats[newX][newY] == "#":
			return 0
		elif seats[newX][newY] == "L":
			return 1
		newX += a
		newY += b
	return 1

def countAllDirections(seats, x, y):
	numEmpty = 0
	for a in range(-1, 2):
		for b in range(-1, 2):
			if a != 0 or b != 0:
				numEmpty += countDirection(seats, x, y, a, b)
	return numEmpty

file = open("seats.txt", "r")
seats = [line[:-1] for line in file]
change = True
while change:
	newSeats = []
	change = False
	for x in range(len(seats)):
		newRow = []
		for y in range(len(seats[x])):
			if seats[x][y] == "L" and countAllDirections(seats, x, y) == 8:
				newRow.append("#")
				change = True
			elif seats[x][y] == "#" and countAllDirections(seats,x,y) <= 3:
				newRow.append("L")
				change = True
			else:
				newRow.append(seats[x][y])
		newSeats.append(newRow)
	seats = newSeats
occupied = sum([row.count("#") for row in seats])
print(occupied)