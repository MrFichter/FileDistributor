def splitString (origString, splitPoint):
    '''Splits origString into beforeSplit and afterSplit. \
The splitPoint is a character somewhere within origString. \
Example: splitPoint might be a period separating the file \
name from the file type. NB: If there are two periods in \
origString, the program treats the first as the splitPoint.'''

    #Find location of splitPoint.
    for i in range (0, len(origString) ):
        if origString[i] == '.':
            splitLocation = i 
            #Assign characters before splitPoint to string called beforeSplit.
            beforeSplit = origString [0 : splitLocation]
            #Assign characters after splitPoint to string called afterSplit.
            afterSplit = origString [ (splitLocation + 1) : ] # I added +1 to splitLocation because I do not want to include the splitLocation character.
            return (beforeSplit, afterSplit)
