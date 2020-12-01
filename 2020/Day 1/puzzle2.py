# O(n^2)

file = open("expenses.txt", "r")
lines = file.readlines()
numbers = []
for num in lines:
	numbers.append(int(num))
numbers.sort()
for x in range(len(numbers)):
	l = x+1
	r = len(numbers)-1
	while l<r:
		sum = numbers[x] + numbers[l] + numbers[r]
		if sum == 2020:
			print(numbers[x]*numbers[l]*numbers[r])
			exit()
		elif sum < 2020:
			l += 1
		elif sum > 2020:
			r -= 1
print("No solution")