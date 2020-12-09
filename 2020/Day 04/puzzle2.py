# O(n*p)
# n = number of lines
# p = number of key-value pairs in line

import copy

file = open("passports.txt", "r")
valid = 0
requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
eyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
passport = copy.copy(requiredFields)
for line in file:
	if len(line) == 1:
		valid += len(passport) == 0
		passport = copy.copy(requiredFields)
	pairs = line.split()
	for p in pairs:
		key,value = p.split(":")
		if value[-1] == '\n':
			value = value[:-1]
		if (key == "byr" and len(value) == 4 and 1920 <= int(value) <= 2002) or \
		   (key == "iyr" and len(value) == 4 and 2010 <= int(value) <= 2020) or \
		   (key == "eyr" and len(value) == 4 and 2020 <= int(value) <= 2030) or \
		   (key == "hgt" and ((value[-2:] == "cm" and 150 <= int(value[:-2]) <= 193) or \
							  (value[-2:] == "in" and 59 <= int(value[:-2]) <= 76))) or \
		   (key == "hcl" and len(value) == 7 and value[0] == "#" and \
		   		False not in [(48 <= ord(value[c]) <= 57) or (97 <= ord(value[c]) <= 102) for c in range(1,7)]) or \
		   (key == "ecl" and value in eyeColors) or \
		   (key == "pid" and len(value) == 9 and value.isnumeric()):
			passport.remove(key)
valid += len(passport) == 0
print(valid)