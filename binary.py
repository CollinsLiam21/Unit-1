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
print(eighth, seventh, sixth, fifth, fourth, third, second, first)
