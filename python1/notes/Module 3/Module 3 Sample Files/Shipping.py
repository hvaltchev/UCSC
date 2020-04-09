# Shipping expense

def calculateShipping(country, nWidgets):

    if (country == 'USA') or (country == 'US') or (country == 'United States'):
        if nWidgets < 50:
            shippingCost = 6.25
        elif nWidgets < 100:
            shippingCost = 9.50
        elif nWidgets < 150:
            shippingCost =12.75
        else:
            shippingCost = 15.00

    elif country == 'Canada':
        if nWidgets < 50:
            shippingCost = 8.25
        elif nWidgets < 100:
            shippingCost = 12.50
        elif nWidgets < 150:
            shippingCost = 18.00
        else:
            shippingCost = 25.00

    else:
        shippingCost = -1  #  special value to say that we don't ship to this country

    return shippingCost


# Get user input then call the above function

userCountry = input('What country are you shipping to? ')
countOfWidgets = input('How many widgets? ')

#convert to int
countOfWidgets = int(countOfWidgets)

#call the function to see how much it will cost to ship
amountForShipping = calculateShipping(userCountry, countOfWidgets)
if amountForShipping > 0:
    print('It will cost $', amountForShipping, 'to ship your package')
else:
    print('Sorry, we do not ship to', userCountry)
    

