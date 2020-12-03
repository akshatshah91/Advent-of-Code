# O(n)
# n = number of lines in file

file = open("map.txt", "r")
trees = 0
index = 0
for line in file:
	trees += line[index] == '#'
	index = (index + 3) % (len(line)-1)
print(trees)