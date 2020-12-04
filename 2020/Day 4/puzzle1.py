# O(n*p)
# n = number of lines
# p = number of key-value pairs in line

import copy

file = open("passports.txt", "r")
valid = 0
requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
passport = copy.copy(requiredFields)
for line in file:
	if len(line) == 1:
		valid += len(passport) == 0
		passport = copy.copy(requiredFields)
	pairs = line.split()
	for p in pairs:
		key = p[:p.index(":")]
		if key in passport:
			passport.remove(key)
valid += len(passport) == 0
print(valid)