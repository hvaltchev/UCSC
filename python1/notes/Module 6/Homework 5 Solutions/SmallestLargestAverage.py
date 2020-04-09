# Input a list of numbers, find min, max, total, and average

myList = []  # start with an empty list
while True:
    usersInput = raw_input('Please enter a number (RETURN/ENTER when done): ')
    if usersInput == '':
        break
    floatingNumber = float(usersInput)
    myList.append(floatingNumber)


#Initialize variables
nMax = myList[0]
nMin = myList[0]
total = 0.0

for thisValue in myList:
    if thisValue > nMax:
        nMax = thisValue

for thisValue in myList:
    if thisValue < nMin:
        nMin = thisValue

for thisValue in myList:
    total = total + thisValue

avg = total / len(myList)

print "The numbers entered were:"
print myList
print
print "Minimum value was: " + str(nMin)
print
print "Maximum value was: " + str(nMax)
print
print "The total is: " + str(total)
print
print "Averge value was: " + str(avg)



