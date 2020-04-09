# Generate the absolute value of a number:

# Function to determine generate the absolute value
def absoluteValue(valueIn):
    if valueIn >= 0 :
        valueOut = valueIn
    else:
        valueOut = -1 * valueIn
    return valueOut

#Test cases
result = absoluteValue(10.5)
print('The absolute value of 10.5 is', result)
    
result = absoluteValue(-8)
print('The absolute value of -8 is', result)

# Get user input and convert to a floating point number
userNumber = input('Enter a number: ')
userNumber = float(userNumber)

# Call the function with the user's number and print the answer
result = absoluteValue(userNumber)
print('The absolute value of', userNumber, 'is', result)

