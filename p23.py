
"""
def print2(str1):
    print(str1)
    print("This is "+str1)

print2("Moyeen")


def factorial(n):
    fac=1
    for i in range (n):
        fac = fac * (i+1)
    return fac
    pass
number = int (input("Enter number "))
print(factorial(number))

def factorial_recursive(n):
    fac=1
    for i in range (n):
        fac = fac * (i+1)
    return fac
    pass
"""

def factorial_recursive(n):
if n ==1:
    return 1
else:
    return n * factorial_recursive(n-1)

number = int (input("Enter number "))
print(factorial(number))
print("Factorial Using interative Method",