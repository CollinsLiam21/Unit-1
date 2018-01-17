#Liam Collins
#1/17/18
#nameAge.py

name = input('Enter first and last name ')
age = int(input('Enter you age '))

name1, name2 = name.split()
len(name1)
len(name2)
print('Your first name has', len(name1), 'letters in it')
print('Your last name has', len(name2), 'letters in it')
print('You will be', age+1, 'next year')
