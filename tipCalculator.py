#Liam Collins
#1/17/18
#tipCalculator.py - Calculating tip

price = float(input('Price of Meal '))
percent = float(input('% to tip '))

print('You should tip', round(price*percent/100,2), 'dollars')
