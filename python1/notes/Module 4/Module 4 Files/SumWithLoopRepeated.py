# Calculate sum - repeated 

def calculateSum(target):
    total = 0
    nextNumberToAddIn = 1
    while nextNumberToAddIn <= target:
        # add in the next value
        total = total + nextNumberToAddIn
        #increment 
        nextNumberToAddIn = nextNumberToAddIn + 1
    return total


answer = 'y'
while answer == 'y':
    userTarget = input('Enter a target number: ')
    userTarget = int(userTarget)
    userTotal = calculateSum(userTarget)

    print('The sum of the numbers from 1 to', userTarget, 'is:', userTotal)

    answer = input('Do you want to try again (y/n)? ')

print('OK Bye')
