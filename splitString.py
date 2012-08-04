def splitString (OrigString, splitPoint):
	'''Splits OrigString into charsBeforeSplitPoint and charsAfterSplitPoint. splitPoint is a character somewhere within OrigString. Example: splitPoint might be a period separating the file name from the file type.'''

	#initialize variables
	charsBeforeSplitPoint = ''
	charsAfterSplitPoint = ''
	haveEncounteredSplitPoint = False

	for character in OrigString: ##Loops through each character in the string
		if character == 'splitPoint':
			haveEncounteredSplitPoint = True #This helps us keep track of whether we're working with characters before or after the splitPoint.

		if character != 'splittingPoint': #Every character except for splittingPoint gets assigned to a new string.

			##If a character comes after the splitting point, it will become part of the string called charsAfterSplit.
			if haveEncounteredSplitPoint:
				charsAfterSplitPoint += character

			##If a character comes before the splitting point, it will become part of the string called charsAfterSplit.
			elif not haveEncounteredSplitPoint:
				charsBeforeSplitPoint += character

	return (charsBeforeSplitPoint, charsAfterSplitPoint)
