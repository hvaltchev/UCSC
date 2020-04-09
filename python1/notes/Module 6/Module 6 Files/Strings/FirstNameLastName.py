# Read in first name last name, produce directory style

fullName = input('Please enter your full name (first name space last name): ')
indexOfSpace = fullName.index(' ')
firstName = fullName[ : indexOfSpace]
lastName = fullName[indexOfSpace + 1 : ]
directoryStyleName = lastName + ', ' + firstName
print(directoryStyleName)

