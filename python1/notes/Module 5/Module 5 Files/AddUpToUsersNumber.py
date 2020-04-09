# Calculate the total of numbers up to a number entered by the user

usersNumber = input('Please enter a number: ')
usersNumber = int(usersNumber)


total = 0
for number in range(1, usersNumber + 1):
    total = total + number

print('The total numbers from 1 to', usersNumber, 'is', total)
    
