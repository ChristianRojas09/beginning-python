import sys


#Request Rental code:

rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n").upper()

#Request time period the car was rented.

if rentalCode == 'B' or rentalCode == 'D':
  rentalPeriod = int(input("Number of days rented:\n"))
else:
  rentalPeriod = int(input("Number of weeks rented:\n"))
#print(rentalCode)
#print(rentalPeriod)

##Set the base charge for the rental type 

budgetCharge = 40.00
dailyCharge = 60.00
weeklyCharge = 190.00

if rentalCode == 'B':
  baseCharge = float(rentalPeriod * budgetCharge)
elif rentalCode == 'D':
  baseCharge = float(rentalPeriod * dailyCharge)
elif rentalCode == 'W':
    baseCharge = float(rentalPeriod * weeklyCharge)
#print(format(baseCharge, ",.2f"))



#4)Collect Mileage information:

rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n").upper()

# collect the starting mileage

odoStart = input("Starting Odometer Reading:\n")

# record the ending mileage

odoEnd = input("Ending Odometer Reading:\n")

#c) Calculate total miles

totalMiles = int(odoEnd) - int(odoStart)



##	Calculate the mileage charge and store it as 
#   the variable mileCharge:
mileCharge = 0
extraMiles = 0

if rentalCode == 'B':
  mileCharge = 0.25 * totalMiles
#print(format(mileCharge, ",.2f"))

if rentalCode == 'D':
  averageDayMiles = int(totalMiles)/int(rentalPeriod)
  if averageDayMiles <= 100:
    totalMiles = 0
  elif averageDayMiles > 100:
    extraMiles = averageDayMiles - 100
  mileCharge = 0.25 * extraMiles  

if rentalCode == 'W':
  averageWeekMiles = int(totalMiles)/int(rentalPeriod)
  if averageWeekMiles <= 900:
    mileCharge = 0
  elif averageWeekMiles > 900:
    mileCharge = 100 * int(rentalPeriod)  
amtDue = int(baseCharge) + int(mileCharge)

# Print final results:

amtDue = baseCharge + float(mileCharge)
print('Rental Summary')
print('Rental Code: '+ str(rentalCode))
print('Rental Period: '+ str(rentalPeriod))
print('Starting Odometer: '+ str(odoStart))
print('Ending Odometer: '+ str(odoEnd))
print('Miles Driven: '+ str(totalMiles))
print('Amount Due: '+'${:,.2f}'.format(amtDue))