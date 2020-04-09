# Read multiple lines of text from a file

from FileReadWrite import *

DATA_FILE_PATH = 'MultiLineData.txt'

myFileHandle = openFileForReading(DATA_FILE_PATH)

line1 = readALine(myFileHandle)
line2 = readALine(myFileHandle)
line3 = readALine(myFileHandle)   # contains several pieces of information

# Third line consists of a string, an integer, and a float

closeFile(myFileHandle)
print('First line:', line1)
print('Second line:', line2)

# Split up the third line into 3 pieces of information, name, height, weight
dataList = line3.split(',')
name = dataList[0]
height = float(dataList[1])
weight = int(dataList[2])

print('Data from third line:', name, height, weight)




