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

        firstLast = str(self.cornerChar) + str(self.hChar) * (self.size - 2) + str(self.cornerChar)
        middle = str(self.vChar) + (' ' * (self.size - 2)) + str(self.vChar)

        for x in range(0, self.size):
            if x == 0 or x == self.size - 1:
                print(firstLast)
            else:
                print(middle)

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

class Rectangle():
    """Represents a rectangle
    """
    def __init__(self, length, width, hChar, vChar, cornerChar):
        ''' Initializes a rectangle
     in the size, the character to used for the horizontal edge, vertical edge, and corners.
        '''
        self.length = length
        self.width = width
        self.hChar = hChar
        self.vChar = vChar
        self.cornerChar = cornerChar

    def show(self):
        ''' Print the square in text using the horizontal edge, vertical edge, and corner characters
        Use a space (' ') for all characters not on an edge
        '''
        print()
        firstLast = str(self.cornerChar) + str(self.hChar) * (self.length - 2) + str(self.cornerChar)
        middle = str(self.vChar) + (' ' * (self.length - 2)) + str(self.vChar)

        for x in range(0, self.width):
            if x == 0 or x == self.width - 1:
                print(firstLast)
            else:
                print(middle)

    def getLength(self):
        ''' Returns the size of an edge of the Square '''
        return self.length

    def setLength(self, length):
        self.length = length

    def getWidth(self):
        ''' Returns the size of an edge of the Square '''
        return self.width

    def setWidth(self, width):
        self.length = width

    def getArea(self):
        return self.length * self.width

    def getPerimeter(self):
        return 2 * (self.length + self.width)

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
print('Size is:', oSquare1.getSize(), " Area is:", oSquare1.getArea())

# Create another square of size 10
oSquare2 = Square(10, '-', '|', '*')
oSquare2.show()
print('Size is:', oSquare2.getSize(), " Area is:", oSquare2.getArea())

# Tell the first square to modify its data
oSquare1.setSize(7)
oSquare1.setHorizontalChar('^')
oSquare1.setVerticalChar('?')
oSquare1.setCornerChar('$')
oSquare1.show()
print('Size is:', oSquare1.getSize(), " Area is:", oSquare1.getArea())
print()

# Add code here to ask the user questions, and create and show a new Square based on the answers
size = int(input('What is the (integer) size of an edge of a square: '))
hChar =input('What character to use for the horizontal edges: ')
vChar = input('What character  to use for the vertical edges: ')
cChar = input('What character  to use for the corners: ')

oSquare3 = Square(size, hChar, vChar, cChar)
oSquare3.show()
print('Size is:', oSquare3.getSize(), " Area is:", oSquare3.getArea())
print()

# Test code for Rectangle
length = int(input('What is the (integer) length of the Rectangle: '))
width = int(input('What is the (integer) width of the Rectangle: '))
hChar = input('What character to use for the horizontal edges: ')
vChar = input('What character to use for the vertical edges: ')
cChar = input('What character to use for the corners: ')

oRectangle1 = Rectangle(length, width, hChar, vChar, cChar)
oRectangle1.show()
print('Perimeter is:', oRectangle1.getPerimeter(), " Area is:", oRectangle1.getArea())
print()
