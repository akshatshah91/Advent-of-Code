# O(n*k)
# n - number of passwords
# k - length of passwords

import re

file = open("passwords.txt", "r")
valid = 0
for l in file:
	low,high,letter,password = re.split("-| |: ", l)
	valid += int(int(low) <= password.count(letter) <= int(high))
print(valid)