'''
a = input()
print('a='+a)
b = input()
print('b='+b)
if a<b:
    print('a='+b)
    print('b='+a)
elif a > b:
    print('b='+b)

import cmath
a = 1
b= 5
c= 10
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('Solution is '.format(sol1,sol2))


import cmath

a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

# calculate the discriminant
d = (b ** 2) - (4 * a * c)

# find two solutions
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)
print('The solution are {0} and {1}'.format(sol1, sol2))

celsius_2 = float (input("Temperature values in degree celsius:"))
Fahrenheit_2 = (celsius_2 * 9/5)+32
print('the %2f degree Celsius is equal to : %2f Fahrenheit'%(celsius_2,Fahrenheit_2))
'''
Fahrenheit_2 = float(input("tempeture value in degree Fahrenheit :"))
celsius_2 = (Fahrenheit_2 - 32)*5/9
print ('The %.2f degree Fahrenheit is equal to : %2f celsius'%(Fahrenheit_2,celsius_2))
