file = open("ingredients.txt", "r")
ingredients = {}
allergens = {}
for line in file:
	i,a = line[:-2].split(" (contains ")
	i = i.split(" ")
	for food in i:
		if food in ingredients:
			ingredients[food][0] += 1
		else:
			ingredients[food] = [1, None]
	a = a.split(", ")
	for allergy in a:
		if allergy in allergens:
			for x in range(len(allergens[allergy])-1, -1, -1):
				food = allergens[allergy][x]
				if food not in i:
					allergens[allergy].remove(food)
			if len(allergens[allergy]) == 1:
				ingredients[allergens[allergy][0]][1] = allergy
		else:
			allergens[allergy] = i.copy()
for x in range(len(allergens.keys())):
	for k in allergens.keys():
		newList = []
		for i in allergens[k]:
			if ingredients[i][1] == None or ingredients[i][1] == k:
				newList.append(i)
		if len(newList) == 1:
			ingredients[newList[0]][1] = k
		allergens[k] = newList
dangerous = [x for _,x in sorted(zip(allergens.keys(), allergens.values()))]
avoid = ""
for x in range(len(dangerous)):
	avoid += dangerous.pop(0)[0] + ","
print(avoid[:-1])