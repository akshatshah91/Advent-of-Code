def play(deck1, deck2, pastDecks):
	while len(deck1) > 0 and len(deck2) > 0:
		winner = None
		if (deck1,deck2) in pastDecks:
			return 1,deck1
		pastDecks.append((deck1[:],deck2[:]))
		card1 = deck1.pop(0)
		card2 = deck2.pop(0)
		if card1 <= len(deck1) and card2 <= len(deck2):
			winner,_ = play(deck1[:card1], deck2[:card2], pastDecks[:])
		else:
			if card1 > card2:
				winner = 1
			else:
				winner = 2
		if winner == 1:
			deck1 += [card1, card2]
		else:
			deck2 += [card2, card1]
	if len(deck1) == 0:
		return 2,deck2
	else:
		return 1,deck1

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
_,winner = play(deck1, deck2, [])
winner.reverse()
points = 0
for x in range(len(winner)):
	points += (x+1) * winner[x]
print(points)