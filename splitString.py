def splitString (origString, splitPoint):
    '''Splits origString into beforeSplit and afterSplit. The splitPoint is a character somewhere within origString. Example: splitPoint might be a period separating the file name from the file type.'''

    #Find location of splitPoint.
    i = 0
    for character in origString:
        if character == '.':
            splitLocation = i
        else: i += 1

    #Assign characters before splitPoint to string called beforeSplit.
    beforeSplit = origString [0 : splitLocation]

    #Assign characters after splitPoint to string called afterSplit.
    afterSplit = origString [ (splitLocation + 1) : ] # I added +1 to splitLocation because I do not want to include the splitLocation character.
               
    return (beforeSplit, afterSplit)
