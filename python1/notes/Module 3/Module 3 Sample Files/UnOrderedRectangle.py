# Determine if a side1, side2, side3, and side4 (unordered) represent a Rectangle or not:

# Function to determine if four sides represent a Rectangle
# Two pairs of sides must be equal
def isRectangle(side1, side2, side3, side4):
    if (side1 == side2) and (side3 == side4):
        return True
    if (side1 == side3) and (side2 == side4):
        return True
    if (side1 == side4) and (side2 == side3):
        return True
    if (side1 == side2) and (side3 == side4):
        return True
    return False

#Test cases
if isRectangle(2, 4, 2, 4):
    print('2, 4, 2, 4 is a Rectangle')
else:
    print('2, 8, 2, 8 is not a Rectangle')
    
if isRectangle(2, 4, 4, 2):
    print('2, 4, 4, 2 is a Rectangle')
else:
    print('2, 8, 2, 8 is not a Rectangle')
    
if isRectangle(2, 7, 2, 9):
    print('2, 7, 2, 9 is a Rectangle')
else:
    print('2, 7, 2, 9 is not a Rectangle')
     

# Get user input and call the function.
userSide1 = input('Enter the side1: ')
userSide1 = int(userSide1)
userSide2 = input('Enter the side2: ')
userSide2 = int(userSide2)
userSide3 = input('Enter the side3: ')
userSide3 = int(userSide3)
userSide4 = input('Enter the side4: ')
userSide4 = int(userSide4)

# Let's assign the result of calling the funtion to a boolean variable,
# then check the variable in the if statement
userRectangle = isRectangle(userSide1, userSide2, userSide3, userSide4)
if userRectangle:
    print(userSide1, userSide2, userSide3,  userSide4, 'is a Rectangle')
else:
    print(userSide1, userSide2, userSide3,  userSide4, 'is not a Rectangle')


