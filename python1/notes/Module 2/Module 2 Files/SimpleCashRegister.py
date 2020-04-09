# Simple cash register

cost = input('Please enter the cost of the item: ')
cost = float(cost)
cash = input('Please enter the cash given: ')
cash = float(cash)
change = cash - cost
print('Your item costs', cost, 'and you gave me', cash, 'dollars. Your change is', change)
