def findLongestTrain(startNum):
	dominoes = [[5,1], [10,6], [6, 4], [12, 10], [10, 5], [12, 3], [12, 5], [7, 7], [10, 10], [9, 6], [10, 7], [8, 6], [6, 2], [7, 5]]
	startDoms = []

	for d in dominoes:
		if startNum in d:
			startDoms.append(d)


	if len(startDoms) == 0:
		print "You have no possible trains :("
		return

	doms = []
	finalTrain = []
	newTrain = []

	for d in startDoms:
		doms = [x for x in dominoes if x != d]
		if d[0] == startNum:
			newTrain = findNext(doms, d[1], [d])
		else:
			newTrain = findNext(doms, d[0], [d])

		if len(newTrain) > len(finalTrain):
			finalTrain = newTrain

	print finalTrain


def findNext(domsLeft, domNumToMatch, train):
	found = False
	newTrain = []
	finalTrain = []

	for d in domsLeft:
		if domNumToMatch in d:
			found = True
			newDomsLeft = [x for x in domsLeft if x != d]
			if d[0] == domNumToMatch:
				newTrain = findNext(newDomsLeft, d[1], train + [d])
			else:
				newTrain = findNext(newDomsLeft, d[0], train + [d])
		
			if len(newTrain) > len(finalTrain):
				finalTrain = newTrain

	if found == False:
		return train
	else:
		return finalTrain

findLongestTrain(6)

