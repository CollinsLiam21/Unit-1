#Liam Collins
#1/19/18
#change.py

totalCents = int(input('Enter number of cents: '))

quarter = totalCents//25
print(quarter, 'quarters')

dime = (totalCents-(quarter*25))//10
print(dime, 'dime')

nickel = (totalCents-(quarter*25)-(dime*10))//5
print(nickel, 'nickels')

penny = (totalCents-(quarter*25)-(dime*10)-(nickel*5))
print(penny, 'pennies')
