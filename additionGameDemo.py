#Liam Collins
#1/22/18
#additionGameDemo.py - How to use random numbers

from random import randint

num1 = randint(-10,10)
num2 = randint(-10,10)
ans = int(input(str(num1) + '+' + str(num2) + '= '))
print(ans == num1+num2)

