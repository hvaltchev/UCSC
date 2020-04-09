#  Python program to calculate the cost of tickets for a show at school

COST_PER_ADULT_TICKET = 10 
COST_PER_CHILD_TICKET = 5

def calculateCost(nAdults, nChildren, isStudent):
    total = (nAdults * COST_PER_ADULT_TICKET) + (nChildren * COST_PER_CHILD_TICKET)
    if isStudent:
        total = total * .85      #  15% discount is same as paying 85%

    return total

print calculateCost(2, 5, False)
print calculateCost(2, 1, True)
print calculateCost(0, 8, False)
print calculateCost(3, 3, True)
print calculateCost(6, 0, True)

userAdultTix = raw_input("Enter number of adults tickets: ")
userAdultTix = int(userAdultTix)
userChildTix = raw_input("Enter number of childr tickets: ")
userChildTix = int(userChildTix)
userIsStudent = raw_input("Are you a student? (y/n) ")
if userIsStudent == 'y':
    userIsStudent = True
else:
    userIsStudent = False

#  Could also write:     userIsStudent = (userIsStudent == 'y')
 
print calculateCost(userAdultTix, userChildTix,userIsStudent)



       
