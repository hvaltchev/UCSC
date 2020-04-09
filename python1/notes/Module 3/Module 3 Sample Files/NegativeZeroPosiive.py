# Determine if a number is negative, zero, or positive

# Function to determine neg, zero, or positive
# It returns an appropriate string
def negativeZeroPositive(value):

    if value < 0.0:
        return 'negative'
    elif value > 0.0:
        return 'positive'
    else:
        return 'zero'

#Test cases
result = negativeZeroPositive(-25.7)
print('-25.7 is', result)
    
result = negativeZeroPositive(0.0)
print('0.0 is', result)

result = negativeZeroPositive(123.45)
print('123.45 is', result)
     

# Get user input and call the function.
userValue = input('Enter a number: ')
userValue = float(userValue)
userResult = negativeZeroPositive(userValue)
print(userValue, 'is', userResult)



