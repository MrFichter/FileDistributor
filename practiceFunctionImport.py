from splitString import splitString 
# From (filename with .py chopped off) import (function, in this case.)

fileName, fileType = splitString ('fractions.sb' , '.')
print 'fileName is ' , fileName
print 'fileType is ' , fileType
