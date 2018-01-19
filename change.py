#Liam Collins
#1/19/18
#change.py

totalCents = int(input('Enter number of cents: '))

quarter = round(totalCents/25,0)
print(quarter)

nickel = round((totalCents-(quarter*25))/5,0)
print(nickel)

penny = round((totalCents-(quarter*25)-(nickel*5)),0)
print(penny)