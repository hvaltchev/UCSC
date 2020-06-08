while True:
    try:
        name = str(input('Name Please: '))
        money = int(input('How much money do you have? '))
        money = money / 2
        money = str(money)
        print(name + ' give me $' + money)
    except ValueError:
        print('Please try again.')

