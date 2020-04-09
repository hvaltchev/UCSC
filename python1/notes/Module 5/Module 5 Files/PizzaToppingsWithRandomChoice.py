# Pizza topping program

import random

randomToppings = ['pineapple', 'pepperoni', 'mushrooms', \
                  'bacon', 'onions', 'anchovies', 'artichokes', \
                  'tomatoes']

# Function to show the list of toppings
def showPizzaToppings(theList):
    print()
    if len(theList) == 0:
        print('Your pizza has no toppings.')
    else:
        print('The toppings on your pizza are:')
        print()
        for thisItem in theList:  # iterate through the list, print each item
            print('   ' + thisItem)
    print() #blank line

#main code
print('Welcome to my Pizzeria, where you get to choose your toppings.')
print('When prompted, enter the first letter or the full word what you want to do.')
print()
print('---- Operations ----')
print('a/add           Add a topping')
print('c/change      Change a topping')
print('o/order         Order the pizza')
print('p/pick           Pick a random topping for you')
print('q/quit           Quit')
print('r/remove       Remove a topping')
print('s/startover    Start over')
print

#main code
toppingsList = [ ]
showPizzaToppings(toppingsList)
while True:

    menuChoice = input('   add, change, order, quit, pick, remove, startover: ')


    if (menuChoice == 'a') or (menuChoice == 'add'):  #add a topping
        newTopping = input('Type in a topping to add: ')
        toppingsList.append(newTopping)  #append adds to the end of a list
        
    elif (menuChoice == 'c') or (menuChoice == 'change'):  #change a topping
        oldTopping = input('What topping would you like to change: ')
        if oldTopping in toppingsList:  # is it in the list
            index = toppingsList.index(oldTopping)  #find out where it is in the list
            newTopping = input('What is the new topping: ')
            toppingsList[index] = newTopping   # set a new value at that index
        else:
            print(oldTopping, 'was not found.')

    elif (menuChoice == 'o') or (menuChoice == 'order'):  #order the pizza
        showPizzaToppings(toppingsList)
        print()
        print('Thanks for your order!')
        print()
        another = input('Would you like to order another pizza (y/n) ? ')
        if another == 'y':
            toppingsList = [ ]
        else:
            break

    elif (menuChoice == 'p') or (menuChoice == 'pick'):  #pick random
        randomTopping = random.choice(randomToppings)
        print('For you, I randomly chose to add: ', randomTopping)
        print('and added it to your toppings.')
        toppingsList.append(randomTopping)

    elif (menuChoice == 'q') or (menuChoice == 'quit'): #quit
        break
    
    elif (menuChoice == 'r') or (menuChoice == 'remove'):  #remove a topping
        delTopping = input('What topping would you like to remove: ')
        if delTopping in toppingsList:  #check to see if the topping is in our list
            index = toppingsList.index(delTopping)  # find out where it is
            toppingsList.pop(index)    # remove it
                                    #  same as: del toppingsList[index]
                                    #  same as:  toppingsList.remove(delTopping)
            # The code above only removes the first occurrence of the topping.  
        else:
            print(delTopping, 'was not found')
            
    elif (menuChoice == 's') or (menuChoice == 'startover'):  #reset to no toppings
        print("OK, let's start over.")
        toppingsList = [ ]  #reset to the empty list

    else:
        print("Uh ... sorry, I'm not sure what you said, please try again.")

    showPizzaToppings(toppingsList)  # show the list of toppings on the pizza
 
print()
print('Goodbye')
