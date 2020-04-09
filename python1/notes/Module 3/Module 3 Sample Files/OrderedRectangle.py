# Determine if the four side lengths represent a Rectangle or not:

# Function to determine if four sides represent a Rectangle
# Is a rectangle if left is the same as the right
# and top is the same as the bottom
def isRectangle(left, top, right, bottom):
    if left == right:
        if top == bottom:
            return True
    return False

#Test cases
if isRectangle(2, 8, 2, 8):
    print('2, 8, 2, 8 is a Rectangle')
else:
    print('2, 8, 2, 8 is not a Rectangle')
    
if isRectangle(2, 7, 2, 9):
    print('2, 7, 2, 9 is a Rectangle')
else:
    print('2, 7, 2, 9 is not a Rectangle')
     

# Get user input and call the function.
userLeft = input('Enter the left: ')
userLeft = int(userLeft)
userTop = input('Enter the top: ')
userTop = int(userTop)
userRight = input('Enter the right: ')
userRight = int(userRight)
userBottom = input('Enter the bottom: ')
userBottom = int(userBottom)

# Let's assign the result of calling the funtion to a boolean variable,
# then check the variable in the if statement
userRectangle = isRectangle(userLeft, userTop, userRight, userBottom)
if userRectangle:
    print(userLeft, userTop, userRight,  userBottom, 'is a Rectangle')
else:
    print(userLeft, userTop, userRight,  userBottom, 'is not a Rectangle')


