"""


def sum(a,b):
    return a+b
c = sum(1,2)
print(c)



def print_my_name(name):
    print('Your name is:'+name)
my_name = input(print("enter your name:"))
print_my_name(my_name)


var = print("ok")
print(type(var))

def fibonacci(n):
    if n==0:
        return 0
    else:
        x=0
        y=1
        print(x)
        print(y)
        for i in range(1,n):
            z=x+y
            x=y
            y=z
            print(z)

fibonacci(4)

import random as r
secrate_age=r.randint(1,10)
flag = True
def game_func(guessed_age,secrate):
    if guessed_age<secrate:
        return 'too low'
    elif guessed_age > secrate:
        return 'too high'
for i in range(1,6):
    print('Take a guess.you have'+str(6-i)+'guesses left.' )
    guess = input()
    if game_func(int(guess),secrate_age) == 'Correct':
        print('you won the game')
        break
if not flag:
    print("you lost the game ")

num= 19
flag = False
if num==1:
    print(num,"is not a prime number")
elif num>1:
    for i in range(2, num):
        if(num%i)==0:
            flag= True
            break
    if flag:
        print(num,"Is not a prime number ")
    else:
        print(num,"is a prime number")


def  C_even_odd(n):
    if n% 2==0:
        print('The numner is even')
    else:
        print("the number is odd ")
n = int(input())
C_even_odd(n)



def compute_fcf(x,y):
    if x>y:
        samller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if((x%i==0) and (y%i==0)):
            hcf = i
    return hcf

num1 = 54
num2 = 24

print("the hcf is ", compute_fcf(num1,num2))



print('hello',end=' ' )
print('world')


print('a','b','c','d')

# we can use golbal in local site
def f():
    c=10
    print(c)
f()
print(c)

def function():
    global a
    print(a+23)
a=10
function()

x=100
print(x)
def pop():
    print(x)

x=10
print(x)
pop()
print(x)
"""

def fun(x):
    try:
        return 100/x
    except:
        return  'There is a zero divisor error'
answer = fun()
print(answer)