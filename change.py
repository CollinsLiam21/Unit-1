#Liam Collins
#1/19/18
#change.py

totalCents = int(input('Enter number of cents: '))

quarter = round(totalCents//25)
print(quarter, 'quarters')

nickel = round((totalCents-(quarter*25))//5)
print(nickel, 'nickels')

penny = round((totalCents-(quarter*25)-(nickel*5)))
print(penny, 'pennies')
