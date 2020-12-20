import operator
ops = { "+": operator.add, "*": operator.mul }

def operate(math, operation):
	x = math.index(operation)
	num = ops[operation](int(math[x-1]), int(math[x+1]))
	return num,x

def evaluate(math):
	while "(" in math:
		low = math.index("(")
		high = None
		paren = 0
		for x in range(low, len(math)):
			if math[x] == "(":
				paren += 1
			elif math[x] == ")":
				paren -= 1
			if paren == 0:
				high = x
				break
		num = evaluate(math[low+1:high])
		math[low] = str(num)
		for y in range(high, low, -1):
			math.pop(y)
	while "+" in math:
		num,x = operate(math, "+")
		math[x-1] = str(num)
		math.pop(x)
		math.pop(x)
	while "*" in math:
		num,x = operate(math, "*")
		math[x-1] = str(num)
		math.pop(x)
		math.pop(x)
	return int(math[0])

file = open("math.txt", "r")
total = 0
for line in file:
	math = [c for c in line[:-1].replace(" ", "")]
	total += evaluate(math)
print(total)