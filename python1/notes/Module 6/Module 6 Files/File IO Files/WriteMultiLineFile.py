# Write multiple lines of text to a file

from FileReadWrite import *

DATA_FILE_PATH = 'MultiLineData.txt'

myFileHandle = openFileForWriting(DATA_FILE_PATH)

data1 = 'Here is some data as a string'
writeALine(myFileHandle, data1)
data2 = 'Here is a second line of string data'
writeALine(myFileHandle, data2)

# Could have some code join several pieces of data into a single string: name height, weight
data3 = 'Joe Schmoe,72.5,182'
writeALine(myFileHandle, data3)

closeFile(myFileHandle)

print('OK, done')
