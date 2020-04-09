# Code to show how you can 'Wrap-around" using a list
import random

# Create some list to move through
myList = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff']

# Find out how many elements there are:
nItems = len(myList)

# Save away index of last element as we will use this in the following code
indexOfLastElement = nItems - 1

# Randomly choose a starting index
index = random.randrange(nItems)

while True:
    # Display the current selection
    print
    print 'Current selection is: ', myList[index]
    print
    direction = raw_input('Press p for previous, n for next, anything else to quit:  ')

    # If the user wants to go the previous element
    if direction == 'p':
        if index == 0:  # if we are at the zeroth index, wrap around to the last index
            index = indexOfLastElement
        else:  # just subtract one to get the to previous index
            index = index - 1

    # if the user wants to go to the next element        
    elif direction == 'n':
        if index == indexOfLastElement:  # if we are at the last element, go to the zeroth element
            index = 0
        else:
            index = index + 1 # just add one to go to the next element
    else:
        break

