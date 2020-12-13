file = open("buses.txt", "r")
time = int(file.readline())
buses = [int(c) for c in file.readline().split(",") if c != "x"]
idNum = buses[0]
wait = time - (time%buses[0])
for x in range(1, len(buses)):
	if buses[x]-(time%buses[x]) < wait:
		wait = buses[x]-(time%buses[x])
		idNum = buses[x]
print(idNum * wait)
