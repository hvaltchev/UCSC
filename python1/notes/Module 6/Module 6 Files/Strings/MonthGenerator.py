# convert month number to string

months = 'JanFebMarAprMayJunJulAugSepOctNovDec'

while True:
    monthNumber = input('Enter a month number: ')
    if monthNumber == '':
        break

    try:
       monthNumber = int(monthNumber)
    except:
        print('Please enter a valid number')
        continue

    if (monthNumber < 1) or (monthNumber > 12):
        print('Please enter a number between 1 and 12')
        continue

    start = (monthNumber -1) * 3
    end = start + 3

    abbrev = months[start : end]

    print(abbrev)

print('Bye')
