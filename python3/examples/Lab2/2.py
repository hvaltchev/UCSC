while True:
    try:
        number = float(input('Number to square please: '))
        digits = int(input('How many digits to the right of the decimal place would you like to have displayed? '))
        print(str(number) + ' squared is ' + number * number)
    except ValueError:
        print('Please try again.')

