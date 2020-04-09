rate = 17.50
totalHours = 55.5
regularHours = 40

overtimeHours = totalHours - regularHours

pay = (rate * regularHours) + ((rate * 1.5) * overtimeHours)

print('For working', totalHours, 'hours, I should be paid $', pay)
