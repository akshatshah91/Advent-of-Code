class Bag:
	def __init__(self, name, parent, children):
		self.name = name
		self.parent = parent
		self.children = children
	def addParent(self, parentName):
		self.parent.append(parentName)
	def setChildren(self, children):
		self.children = children

def countBags(bagsDict, bagName):
	count = 1
	for child in bagsDict[bagName].children.keys():
		count += countBags(bagsDict, child) * bagsDict[bagName].children[child]
	return count

file = open("luggageRules.txt", "r")
bagsDict = {}
for line in file:
	bagName, contains = line.split(" contain ")
	children = {}
	while True:
		if "no other bags." in contains:
			break
		amount = int(contains[:contains.index(" ")])
		if "," in contains:
			childName = contains[contains.index(" ")+1:contains.index(",")]
			if "bags" not in childName:
				childName += "s"
			children[childName] = amount
			contains = contains[contains.index(",")+2:]
		else:
			childName = contains[contains.index(" ")+1:contains.index(".")]
			if "bags" not in childName:
				childName += "s"
			children[childName] = amount
			break
	if bagName in bagsDict:
		bagsDict[bagName].setChildren(children)
	else:
		bagsDict[bagName] = Bag(bagName, [], children)
	for child in children:
		if child in bagsDict:
			bagsDict[child].addParent(bagName)
		else:
			bagsDict[child] = Bag(child, [bagName], {})
print(countBags(bagsDict, "shiny gold bags")-1)