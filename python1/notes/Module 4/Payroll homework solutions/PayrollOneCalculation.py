# Payroll program  - efficient

TIME_AND_A_HALF = 40
DOUBLE_TIME = 60

# Calculate pay given a rate and a number of hours
# Any hours over DOUBLE_TIME is at double the pay
# Any hours over TIME_AND_A_HALF is at time and a half pay
# Remaining is paid at regular rate
def calculatePay(rate, nHours):
    
    if nHours <= 40:
        nDoubleTimeHours = 0
        nTimeAndAHalfHours = 0
        nRegularHours = nHours    
        
    elif nHours <= 60:
        nDoubleTimeHours = 0
        nTimeAndAHalfHours = nHours - 40
        nRegularHours = 40

    else:      #more than 60 hours
        nDoubleTimeHours = nHours - 60
        nTimeAndAHalfHours = 20
        nRegularHours = 40
        
    total = (nDoubleTimeHours * 2 * rate) + (nTimeAndAHalfHours * rate * 1.5) + (nRegularHours * rate)
    return total


# Three sample calls to the above function

theRate = 30
theHours = 20
pay = calculatePay(theRate, theHours)
print 'You worked', theHours, 'at a rate of', theRate, 'per hour, you will be paid $', pay

theRate = 15.50
theHours = 50
pay = calculatePay(theRate, theHours)
print 'You worked', theHours, 'at a rate of', theRate, 'per hour, you will be paid $', pay

theRate = 11
theHours = 70.25
pay = calculatePay(theRate, theHours)
print 'You worked', theHours, 'at a rate of', theRate, 'per hour, you will be paid $', pay

print 
theRate = raw_input('Enter the rate per hour: ')
theRate = float(theRate)
theHours = raw_input('Enter the number of hours: ')
theHours = float(theHours)
pay = calculatePay(theRate, theHours)
print 'You worked', theHours, 'at a rate of', theRate, 'per hour, you will be paid $', pay



