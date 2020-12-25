file = open("decks.txt", "r")
deck1 = []
deck2 = []
nextDeck = False
for line in file:
	if line == "\n":
		nextDeck = True
	elif "Player" in line:
		continue
	elif nextDeck:
		deck2.append(int(line[:-1]))
	else:
		deck1.append(int(line[:-1]))
while len(deck1) > 0 and len(deck2) > 0:
	card1 = deck1.pop(0)
	card2 = deck2.pop(0)
	if card1 > card2:
		deck1.append(card1)
		deck1.append(card2)
	else:
		deck2.append(card2)
		deck2.append(card1)
winner = deck1
if len(deck1) == 0:
	winner = deck2
winner.reverse()
points = 0
for x in range(len(winner)):
	points += (x+1) * winner[x]
print(points)