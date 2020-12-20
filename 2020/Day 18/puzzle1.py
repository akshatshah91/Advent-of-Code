import operator
ops = { "+": operator.add, "*": operator.mul }

def evaluate(math):
	value = 0
	if math[0] == "(":
		value,math = evaluate(math[1:])
	else:
		value = int(math[0])
	while len(math) > 1:
		if math[1] == " " and math[4] == "(":
			paren,newMath = evaluate(math[5:])
			value = ops[math[2]](value, paren)
			math = newMath
		elif math[1] == " ":
			value = ops[math[2]](value, int(math[4]))
			math = math[4:]
		else:
			return value,math[1:]
	return value

file = open("math.txt", "r")
total = 0
for line in file:
	total += evaluate(line[:-1])
print(total)