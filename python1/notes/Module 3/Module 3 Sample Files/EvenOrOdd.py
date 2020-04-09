# Determine if a given integer is even or odd:

# Function to determine if a number is even or odd
def isEven(value):
    if (value % 2) == 0:
        return True
    else:
        return False

#Test cases
if isEven(10):
    print('10 is even')
else:
    print('10 is odd')
    
if isEven(11):
    print('11 is even')
else:
    print('11 is odd')
     

# Get user input and call the function.
userNumber = input('Enter an integer: ')
userNumber = int(userNumber)

# Let's assign the result of calling the funtion to a boolean variable,
# then check the variable in the if statement
userEven = isEven(userNumber)
if userEven:
    print(userNumber, 'is even')
else:
    print(userNumber, 'is odd')

