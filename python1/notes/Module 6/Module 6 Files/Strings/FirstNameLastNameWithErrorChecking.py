# Read in first name last name, produce directory style


while True:
    fullName = input('Please enter your full name (first name space last name): ')
    fullName = fullName.strip() # remove any leading or trailing while space
    nSpaces = fullName.count(' ')
    if nSpaces == 1:  # OK found a single space
        break  # exit the loop
    print('Please try again, make sure that you have one space in your name')
    print()
    
indexOfSpace = fullName.index(' ')
firstName = fullName[ : indexOfSpace]
lastName = fullName[indexOfSpace + 1 : ]
directoryStyleName = lastName + ', ' + firstName

directoryStyleName = directoryStyleName.title()

print(directoryStyleName)
