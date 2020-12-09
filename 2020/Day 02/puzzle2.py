# O(n*k)
# n - number of passwords
# k - length of passwords

import re

file = open("passwords.txt", "r")
valid = 0
for l in file:
	pos1,pos2,letter,password = re.split("-| |: ", l)
	valid += int((password[int(pos1)-1]==letter) ^ (password[int(pos2)-1]==letter))
print(valid)