file = open("buses.txt", "r")
file.readline()
buses = [int(x) for x in file.readline().replace("x", "1").split(",")]
time = 0
index = 1
timeStep = buses[0]
for x in range(1,len(buses)):
	while (time+x)%buses[x] != 0:
		time += timeStep
	timeStep *= buses[x]
print(time)
