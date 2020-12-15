startingNum = [19,0,5,1,10,13]
numberDict = {}
lastNum = None
for x in range(30000000):
    if x < len(startingNum):
        lastNum = startingNum[x]
    elif len(numberDict[lastNum]) > 1:
        lastNum = numberDict[lastNum][-1] - numberDict[lastNum][-2]
    else:
        lastNum = 0
    if lastNum in numberDict:
        numberDict[lastNum].append(x)
    else:
        numberDict[lastNum] = [x]
print(lastNum)