# Determine if a height and width represent a square or not:

# Function to determine if height and width represent a square
def isSquare(height, width):
    if height == width:
        return True
    else:
        return False

#Test cases
if isSquare(2, 8):
    print('2 and 8 is a square')
else:
    print('2 and 8 Is not a square')
    
if isSquare(8, 8):
    print('8 and 8 is a square')
else:
    print('8 and 8 Is not a square')
     

# Get user input and call the function.
userHeight = input('Enter the height: ')
userHeight = int(userHeight)
userWidth = input('Enter the width: ')
userWidth = int(userWidth)

# Let's assign the result of calling the funtion to a boolean variable,
# then check the variable in the if statement
userSquare = isSquare(userHeight, userWidth)
if userSquare:
    print(userHeight, 'and', userWidth, 'is a square')
else:
    print(userHeight, 'and', userWidth, 'is not a square')

