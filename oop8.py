"""
def f():
    print('hello')
f()


def sum(a,b):
    return a+b
a = sum(1,2)
print(a)

def print_my_name(name):
    print('M

def calculation(a,b):
    addition=a+b
    subtraction=a-b
    return addition,subtraction
res=calculation(40, 10)
print(res)


def calculation(a,b):
    return a+b, a-b
add,sub=calculation(40,10)
print(add,sub)



def show_employee(name,salary=9000):
    print("name:",name,"salary:",salary)
show_employee("Ben",12000)
show_employee("Moyeen")



def outer_fan(a, b):
    square =a**2
    def addition(a, b):
     return a+b
    add=addition(a, b)
    return add+5
result=outer_fan(5,10)
print(result)


pi=22/7
degree= float(input("input degrees:"))
radian = degree * (pi/180)
print(radian)


from math import pi
def degrees_to_reds(deg):
    return(deg*pi)/180.0
print(degrees_to_reds(180))
print(degrees_to_reds(90))


base_1 = 5
base_2 = 6
height = float(input("Height of trapezoid :"))
base_1 = float(input("Base one value :"))
base_2 = float(input("Base two value :"))
area = ((base_1 + base_2)/2)*height
print("Aria is ",area)



pi = 22/7
height = float(input('height of Cylinder:'))
rad= float(input('Radius of cylinder :'))
volume = pi * rad * rad * height
sur_area= ((2*pi*rad))*height)((pi*radian**2)*2)
print("Volume is :",volume)
print("Surface is :",sur_area)


pi = 22/7
radian = float(input("Radius of sphere : "))
sur_area = 4*pi*radian**2
volume =(4/3)*(pi*radian **3)
print("Surface area is :",sur_area)
print("volume is :",volume)





def sectorarea():
    pi = 22 / 7
    radius = float(input("radius of circle"))
    angle = float(input('angle measure:'))
    if angle >= 360:
        print("angle is not possible")
        return
    sur_area = (pi * radius ** 2) * (angle / 360)
    print("sector area:", sur_area)
sectorarea()


def discriminant():
    x_value = float(input("the x value:"))
    y_value = float(input("the y value:"))
    z_value = float(input("the z value:"))
    discriminant = (y_value**2) - (4*x_value*z_value)
    if discriminant >0:
        print("Two solutions Discrimemny value is :",discriminant)
    elif discriminant == 0:
        print("one solution,discriminant value is :",discriminant)
    elif discriminant <0:
        print('No real sol',discriminant)
discriminant()


def smallest_multiple(n):
    if (n<=2):
        return n
    i = n*2
    factors = [number for number  in range(n,1,-1)if number*2>n]
    print(factors)
    while True :
        for a in factors :
            if i %a!=0:
                i +=n
                break
                if (a==factors[-1] and i%a == 0):
                    return i

print(smallest_multiple(13))
print(smallest_multiple(11))
print(smallest_multiple(2))
print(smallest_multiple(1))



def sum_difference(n=2):
    sum_0f_squares = 0
    square_of_sum = 0
    for num in range(1,n+1):
        sum_0f_squares += num*num
        square_of_sum += num
    square_of_sum = square_of_sum ** 2
    return square_of_sum - sum_0f_squares
print(sum_difference(12))

"""

def power_base_sum(base,power):
    return sum([int(i) for i in str(pow(base,power))])
print(power_base_sum(2,100))
print(power_base_sum(2,10))

