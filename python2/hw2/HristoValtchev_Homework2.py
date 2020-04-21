#-----------------------------------------------------------------------------------------------#

# Hristo Valtchev
# Homework #2
# 4/21/2020
# Square
#-----------------------------------------------------------------------------------------------#

# Square class - text based
# Allows you to change set initial data, then change the data, and show the square as text
# Because of fonts, squares will probably not show as exactly square

class Square():
    """Represents a square
    """

    def __init__(self, size, hChar, vChar, cornerChar):
        ''' Initializes a square
     in the size, the character to used for the horizontal edge, vertical edge, and corners.
        '''
        self.size = size
        self.hChar = hChar
        self.vChar = vChar
        self.cornerChar = cornerChar

    def show(self):
        ''' Print the square in text using the horizontal edge, vertical edge, and corner characters
        Use a space (' ') for all characters not on an edge
        '''       
        print()
        print('This line should be replaced with lines to draw this Square.')

        for x in range(0, self.size - 1):
            for y in range(0, self.size - 1):
                if (x or y) == 0:
                    print(self.cornerChar)
                if (x or y) == self.size - 1:
                    print(self.cornerChar)
                else:
                    print(self.hChar)

    def getSize(self):
        ''' Returns the size of an edge of the Square '''
        return self.size

    def setSize(self, size):
        self.size = size

    def getArea(self):
        return self.size * self.size

    def setHorizontalChar(self, newHChar):
        ''' Set a new horizontal character '''
        self.hChar = newHChar

        
    def setVerticalChar(self, newVChar):
        ''' Set a new vertical character '''
        self.vChar = newVChar


    def setCornerChar(self, newCornerChar):
        ''' Set a new corner character '''
        self.cornerChar = newCornerChar

# Test code
# Create a square of size 5
oSquare1 = Square(5, '-', '|', '*')  # in size, horizonal, vertical, and edge characters
oSquare1.show()
print('Size is:', oSquare1.getSize(), " area is:", oSquare1.getArea())

# # Create another square of size 10
# oSquare2 = Square(10, '-', '|', '*')
# oSquare2.show()
# print('Size is:', oSquare2.getSize(), " area is:", oSquare2.getArea())

# # Tell the first square to modify its data
# oSquare1.setSize(7)
# oSquare1.setHorizontalChar('^')
# oSquare1.setVerticalChar('?')
# oSquare1.setCornerChar('$')
# oSquare1.show()
# print('Size is:', oSquare1.getSize(), " area is:", oSquare1.getArea())
# print()


# Add code here to ask the user questions, and create and show a new Square based on the answers
