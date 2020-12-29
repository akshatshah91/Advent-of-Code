file = open("keys.txt", "r")
lines = file.readlines()
key1 = int(lines[0])
key2 = int(lines[1])
loops = 0
val = 1
while val != key1:
	val = (val*7) % 20201227
	loops += 1
val = 1
while loops != 0:
	val = (val*key2) % 20201227
	loops -= 1
print(val)