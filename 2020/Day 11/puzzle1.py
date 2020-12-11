def countEmpty(seats, x, y):
	numEmpty = 0
	for a in range(x-1, x+2):
		for b in range(y-1, y+2):
			if a == x and b == y:
				continue
			elif a < 0 or a > len(seats)-1 or b < 0 or b > len(seats[a])-1:
				numEmpty += 1
			elif seats[a][b] == "L" or seats[a][b] == ".":
				numEmpty += 1
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
			if seats[x][y] == "L" and countEmpty(seats, x, y) == 8:
				newRow.append("#")
				change = True
			elif seats[x][y] == "#" and countEmpty(seats,x,y) <= 4:
				newRow.append("L")
				change = True
			else:
				newRow.append(seats[x][y])
		newSeats.append(newRow)
	seats = newSeats
occupied = sum([row.count("#") for row in seats])
print(occupied)