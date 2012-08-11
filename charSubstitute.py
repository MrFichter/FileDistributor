def charSubstitute (text, oldChar, newChar):
    '''Examines each character in a text, replacing instances of oldChar with newChar.'''
    ## Should I prevent bugs by converting text, oldChar, and newChar into strings if they aren't already?

    newText = ''
    for i in range (0 , len (text) ): #Cycle through every character in the text.
        if text[i] == oldChar:
            newText += newChar #Whenever the old character appears, replace it with the new character when you transfer it to newText.
        else:
            newText += text[i] #Otherwise, transfer the character to newText as is.

    return newText
