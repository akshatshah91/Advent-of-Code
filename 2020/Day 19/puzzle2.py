import re

def printDict(rules):
	for k in rules.keys():
		print(k, rules[k])

def addRule(rules, rule):
	line = re.split(": | \| ",rule)
	rules[line[0]] = []
	for y in range(1, len(line)):
		rules[line[0]].append(line[y].replace("\"", "").split(" "))
	return rules

def check(rules, ruleList, text):
	if len(ruleList) == 0:
		return text, True
	for arr in rules[ruleList[0]]:
		newRuleList = arr + ruleList[1:]
		newText = text
		if len(newText) == 0:
			return text, False
		elif arr[0] not in rules:
			if arr[0] == newText[0]:
				newText,success = check(rules, newRuleList[1:], newText[1:])
			else:
				return newText, False
		else:
			newText,success = check(rules, newRuleList, newText)
		if success:
			return newText, success
	return text, False

file = open("rulesAndMessages.txt", "r")
lines = file.readlines()
addedRules = ["8: 42 | 42 8", "11: 42 31 | 42 11 31"]
rules = {}
x = 0
matches = 0
while lines[x] != "\n":
	rules = addRule(rules, lines[x][:-1])
	x += 1
for newLine in addedRules:
	rules = addRule(rules, newLine)
for y in range(x+1, len(lines)):
	newText, success = check(rules, ["0"], lines[y][:-1])
	matches += newText == "" and success
print(matches)