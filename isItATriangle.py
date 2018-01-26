#Liam Collins
#1/22/18
#isItATriangle.py - Working with max(a,b) and min(a,b)

a = float(input('Side A: '))
b = float(input('Side B: '))
c = float(input('Side C: '))

middleSide = a+b+c-max(a,b,c)-min(a,b,c)
print(min(a,b,c)+middleSide>max(a,b,c))