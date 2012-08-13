def slashFormat (rawUserInput):
    '''Converts a string's backslashes to forward \
slashes and makes sure to add a forward slash at the end.'''
    pathConvSlash = rawUserInput.replace('\\' , '/') ##Convert backslashes to forward slashes.
    if pathConvSlash [len(pathConvSlash) - 1] != '/': ## If the final character is not a forward slash...
        formattedPath = pathConvSlash + '/' ##...make sure to add a forward slash at the end.
        return formattedPath
