#Homework 3 

def calculatePay(ratePerHour, nHoursWorked):
    if nHoursWorked <= 40:
        ratePerHour = ratePerHour
        totalPay = nHoursWorked * ratePerHour
        
    elif (nHoursWorked > 40) and (nHoursWorked <= 60):
        extraTimeWorked = nHoursWorked - 40
        ratePerHour = ratePerHour
        totalPay = (40 * ratePerHour) + (extraTimeWorked * (ratePerHour*1.5))
        
    else:
        extraTimeWorked = nHoursWorked - 60
        ratePerHour = ratePerHour
        totalPay = (40 * ratePerHour) + 20 * (ratePerHour * 1.5) + (extraTimeWorked * (ratePerHour*2))
        
    return totalPay

print(calculatePay( 30 , 20 ))
print(calculatePay( 15.5 , 50 ))
print(calculatePay( 11 , 70.25 ))

userInputNumberOfHoursWorked = float(input("Please enter the number of hours worked : "))

userInputRatePerHour = float(input("Please enter the rate per hour : "))

userPay = calculatePay(userInputRatePerHour, userInputNumberOfHoursWorked)

print("The total pay for", userInputNumberOfHoursWorked, "of hours worked with a rate of", userInputRatePerHour, \
      "dollars per hour of", userInputRatePerHour , "is: ", userPay)


#Show cost calculator

ADULT_TICKET_COST = 10
CHILD_TICKET_COST = 5

def calculateCost(nAdultTickets , nChildTickets , isStudent):
    if isStudent == True:
        priceAdultTicket = ADULT_TICKET_COST - (ADULT_TICKET_COST * 0.15)
        priceChildTicket = CHILD_TICKET_COST - (CHILD_TICKET_COST * 0.15)
        totalPaymentTickets = (nAdultTickets * priceAdultTicket) + (nChildTickets * priceChildTicket)

    else :
        ADULT_TICKET_COST
        CHILD_TICKET_COST 
        totalPaymentTickets = (nAdultTickets * ADULT_TICKET_COST) + (nChildTickets * CHILD_TICKET_COST)

    return totalPaymentTickets

print(calculateCost(2, 5, False))
print(calculateCost(2, 1, True))
print(calculateCost(0, 8, False))
print(calculateCost(3, 3, True))
print(calculateCost(6, 0, True))

numberOfAdultTickets = int(input ("Enter the number of adults tickets you want to buy : "))
numberOfChildTickets = int(input ("Enter the number of child tickets you want to buy : "))
userInputIsStudent = input ("Are you Student? yes or no: ")

if (userInputIsStudent=="Y") or (userInputIsStudent=="y") or (userInputIsStudent =='yes') or (userInputIsStudent == 'YES'):
    isStudent = True
else:
    isStudent = False

ticketPrice = calculateCost(numberOfAdultTickets, numberOfChildTickets, isStudent)

print("The total cost for", numberOfAdultTickets, "adult tickets and", numberOfChildTickets, \
      "children tickets is: ", ticketPrice)
