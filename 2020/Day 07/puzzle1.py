class Bag:
	def __init__(self, name, parent, children):
		self.name = name
		self.parent = parent
		self.children = children
	def addParent(self, parentName):
		self.parent.append(parentName)
	def setChildren(self, children):
		self.children = children

file = open("luggageRules.txt", "r")
bagsDict = {}
for line in file:
	bagName, contains = line.split(" contain ")
	children = []
	while True:
		if "no other bags." in contains:
			break
		elif "," in contains:
			childName = contains[contains.index(" ")+1:contains.index(",")]
			if "bags" not in childName:
				childName += "s"
			children.append(childName)
			contains = contains[contains.index(",")+2:]
		else:
			childName = contains[contains.index(" ")+1:contains.index(".")]
			if "bags" not in childName:
				childName += "s"
			children.append(childName)
			break
	if bagName in bagsDict:
		bagsDict[bagName].setChildren(children)
	else:
		bagsDict[bagName] = Bag(bagName, [], children)
	for child in children:
		if child in bagsDict:
			bagsDict[child].addParent(bagName)
		else:
			bagsDict[child] = Bag(child, [bagName], [])
parents = bagsDict["shiny gold bags"].parent
for p in parents:
	newParents = bagsDict[p].parent
	parents += newParents
print(len(set(parents)))