import re

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
rules = {}
x = 0
matches = 0
while lines[x] != "\n":
	line = re.split(": | \| |\n",lines[x])
	rules[line[0]] = []
	for y in range(1, len(line)-1):
		rules[line[0]].append(line[y].replace("\"", "").split(" "))
	x += 1
for y in range(x+1, len(lines)):
	newText, success = check(rules, ["0"], lines[y][:-1])
	matches += newText == "" and success
print(matches)