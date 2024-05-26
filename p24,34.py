
"""def print2(str1):
    print2(str1)
    print("This is " + str1)

print2("Moyeen")
"""

def factorial(n):
    fac =1
    for i in range(n):
        fac = fac * (i+1)
        return fac
number = int(input("Enter the number"))
print(factorial(number))
