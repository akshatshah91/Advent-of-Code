file = open("directions.txt", "r")
xPos = 0
yPos = 0
facing = 1
directions = ["N", "E", "S", "W"]
for line in file:
	instruction = line[0]
	if instruction == "F":
		instruction = directions[facing]
	if instruction == "N":
		yPos += int(line[1:])
	elif instruction == "S":
		yPos -= int(line[1:])
	elif instruction == "E":
		xPos += int(line[1:])
	elif instruction == "W":
		xPos -= int(line[1:])
	elif instruction == "L":
		facing = (facing - (int(line[1:])//90)) % 4
	elif instruction == "R":
		facing = (facing + (int(line[1:])//90)) % 4
print(abs(xPos)+abs(yPos))
