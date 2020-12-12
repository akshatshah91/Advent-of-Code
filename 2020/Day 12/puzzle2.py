def rotate(waypoint, amount):
	for x in range(amount):
		waypoint = [waypoint[1], waypoint[0] * -1]
	return waypoint

file = open("directions.txt", "r")
shipPos = [0, 0]
waypoint = [10, 1]
directions = ["N", "E", "S", "W"]
for line in file:
	instruction = line[0]
	if instruction == "F":
		shipPos = [a + b*int(line[1:]) for a,b in zip(shipPos,waypoint)]
	elif instruction == "N":
		waypoint[1] += int(line[1:])
	elif instruction == "S":
		waypoint[1] -= int(line[1:])
	elif instruction == "E":
		waypoint[0] += int(line[1:])
	elif instruction == "W":
		waypoint[0] -= int(line[1:])
	elif instruction == "L":
		waypoint = rotate(waypoint, 4-(int(line[1:])//90))
	elif instruction == "R":
		waypoint = rotate(waypoint, (int(line[1:])//90))
print(abs(shipPos[0]) + abs(shipPos[1]))