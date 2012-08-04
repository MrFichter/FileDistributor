##File Distributor
##By Jonathan Fichter
##
##This program copies a file of any type
##and distributes it to branch folders.


##MENU / QUESTIONS


import shutil, os


def askYesNo(question):
    """Ask a yes or no question."""
    ## Created by: Mike Dawson.
    response = None
    while response not in ("y", "n"):
        response = raw_input(question).lower()
    return response

### for testing purposes, I am auto-filling responses and commenting out some sections.
sourceFileName = 'FractionsProject.sb'
sourceFilePath = 'C:/Users/Jonathan_2/Desktop/'

####print overview
##
##print '''
##Welcome to this file-distributing program.
##With a little information from you, this
##program will be able to distribute copies
##of a desired file to folders you specify.
##'''
##
####Ask for sourceFileName
##print '''
##To get started, please provide the name
##of the file you wish to copy. Example:
##
##FractionsProject.doc
##
##(NB: This program can only read files
##whose names have no spaces in them.
##Letters and numbers in the file name
##are fine, but special characters
##like symbols and apostrophes may
##cause problems. Before proceeding,
##please consider renaming your file.)
##'''
##sourceFileName = str(raw_input('source file name>'))
##
##### Consider teaching program to automatically correct backslashes the user might input.
##
##
#### Ask for path of sourceFile
##print '''
##Now, please specify the path of this
##file (i.e. where it is located on the
##computer). Please be sure to use forward
##slashes, especially at the end of the
##path name. Example:
##
##C:/Users/Jonathan_2/Desktop/
##'''
##sourceFilePath = str(raw_input('source file path>'))


##Option: Modify file name for each branch folder
print '''
In many situations, you might not want
to create many copies of a file with the
same name. This program provides the option
to alter the file name so that the name of
each copy reflects the folder in which it
resides. For example, you could modify the
file name each time to create the following:

S:/Students/2021/FichterJ/FichterJFractionsProject
S:/Students/2021/MouseM/MouseMFractionsProject
S:/Students/2021/SmithT/SmithTFractionsProject

(See how the original "FractionsProject" file
name gets modified each time?)
'''
modifyOption = askYesNo('Would you like to modify the names of the copied files as described above? y / n>')

### for testing purposes, I am auto-filling responses and commenting out some sections.
baseDestFolder = 'C:/Users/Jonathan_2/Desktop/'
branchFolderNames = 'C:/Users/Jonathan_2/Desktop/sampleTextFileWithThreeNames.txt'

####Ask for base destination folder
##print '''
##Thank you.
##
##* * * * *
##
##When it comes to distributing files,
##this program assumes you have a base
##destination folder from which individual
## folders branch out. For example,
##if you have branch folders like:
##S:/Students/2021/FichterJ ,
##S:/Students/2021/MouseM , and
##S:/Students/2021/SmithT ,
##
##your base folder would be:
##
##S:/Students/2021/
##
##To proceed, please provide the path of
##a base destination folder, making sure
##to use forward slashes as indicated
##above (especially at the end of the
##folder's name).
##'''
##baseDestFolder = str(raw_input('base destination folder>'))
##
##
####Ask for text file with list of branch folder names.
##print '''
##Now, please create a text file (you can
##do this with the Notepad program on your
##computer) in which each line provides
##the name of a folder in which you would
##like a copy of the source file to appear.
##(Please keep in mind: this program
##assumes that each of these folders is a
##branch stemming from the destination base
##folder you just specified.)
##
##The text file you create might look like
##this:
##
##FichterJ
##MouseM
##SmithT
##'''
##print '''
##Now, please enter the file path and name
##of the text file you created. Example:
##
##C:/Users/Jonathan_2/Desktop/branchFolderNames.txt
##'''
##branchFolderNames = str(raw_input('text file path and name>'))
##'''

##COPYING THE FILE AND DISTRIBUTING IT TO DESTINATION FOLDERS


## Loop through the text file of folder names
for line in open (branchFolderNames): 
    
    if modifyOption == 'y': ## i.e. If the user selected
    ##the option to modify the file name for each branch
    ##folder...
        print 'modifyOption = ' + modifyOption ### for testing purposes
        print 'optionalNameMod = ' + optionalNameMod  ### for testing purposes
        optionalNameMod = '/' + sourceFileName + line.strip()
    else: optionalNameMod = ''

    ##In each iteration, the base path remains the same,
    ##but the branch folder changes to reflect the folder
    ## name provided in each line of the text file.
    ##Optionally, the program modifies the file name, too.
    sourceFileComplete = sourceFilePath + sourceFileName    
    destFileComplete = baseDestFolder + line.strip() + optionalNameMod
    try: ##Try and except give us a controlled way of seeing error messages.
        shutil.copy (sourceFileComplete, destFileComplete) ##shutil enables us to copy a file.
    except Exception, e:
        print e
    
    
        


## END
print '''

Thank you for using this program.
'''
raw_input ('Press Enter key to quit.')


###FOR TESTING PURPOSES

##FractionsProject.sb
##C:/Users/Jonathan_2/Desktop/
##C:/Users/Jonathan_2/Desktop/
##C:/Users/Jonathan_2/Desktop/sampleTextFileWithThreeNames.txt






##os.chdir ('C:/Users\Jonathan_2/Desktop/') ##This works, even though the slashes in the middle are weird.
##fileNameFull = 'FractionsProjectFichterJ.sb'


##To check the path:
##import os
##os.getcwd()

##Also try os.chdir()
    
