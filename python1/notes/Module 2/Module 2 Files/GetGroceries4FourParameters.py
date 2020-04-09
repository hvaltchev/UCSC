def separateRuns():
    print('******************')
    print()     #blank line

def getGroceries(storeName, item1, item2, item3):
    # Use the storeName parameter variable
    print('At', storeName, 'I need to buy')
    print(item1)
    print(item2)
    print(item3)
    separateRuns()


# Now call the function with four arguments
getGroceries('Safeway', 'soap', 'lettuce', 'milk')
getGroceries('Luckys', 'milk', 'soda', 'peas')
getGroceries('Amazon.com', 'book', 'dvd', 'cat food')

