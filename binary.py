#Liam Collins
#1/24/18
#binary.py - Binary Numbers

binary = int(input('Enter 8-digit Binary Number: '))

eighth = binary//10000000
seventh = (binary-eighth*10000000)//1000000
sixth = (binary-eighth*10000000-seventh*1000000)//100000
fifth = (binary-eighth*10000000-seventh*1000000-sixth*100000)//10000
fourth = (binary-eighth*10000000-seventh*1000000-sixth*100000-fifth*10000)//1000
third = (binary-eighth*10000000-seventh*1000000-sixth*100000-fifth*10000-fourth*1000)//100
second = (binary-eighth*10000000-seventh*1000000-sixth*100000-fifth*10000-fourth*1000-third*100)//10
first = (binary-eighth*10000000-seventh*1000000-sixth*100000-fifth*10000-fourth*1000-third*100-second*10)//1

decimalNotation = eighth*2**7+seventh*2**6+sixth*2**5+fifth*2**4+fourth*2**3+third*2**2+second*2**1+first*2**0
print(decimalNotation)
print(bin(decimalNotation))
