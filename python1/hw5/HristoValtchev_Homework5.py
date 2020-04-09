#!/usr/bin/env python3

#-----------------------------------------------------------------------------------------------#

# Hristo Valtchev
# Homework #5
# 3/27/2020

#-----------------------------------------------------------------------------------------------#

#Enter a bunch of numbers in a list

numbers = []
while(True):
    number = input("Please Enter a number (RETURN/ENTER when done):")
    if number == '':
        break
    else:
        number = float(number)
        #Store in a list
        numbers.append(number)

#Print the list
for number in numbers:
    print(number)

#Print Sum
total = 0
for number in numbers:
    total += number
print("The sum is:",total)

#Print Average
average = total / len(numbers) 
print("Average value was:", average)

#Print Min
#Print Max
minimum = numbers[0]
maximum = minimum

for number in numbers:
    if minimum > number:
        minimum = number
    if maximum < number:
        maximum = number
print("Minimum value was:", minimum)
print("Maximum value was:", maximum)

