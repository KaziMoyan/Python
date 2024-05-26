"""
l=10
def function1(n):
    #l=5
    m = 8
    #l = l + 45
    global l
    l = l+45
    print(l, m)

    print(n, " i have prientd")
 function1("this is me")
#print(l)
"""
x=89
def Moyeen():
    x=20
    def rohan():
        global x
        x = 88
    print("before calling Kazi()", x)
    rohan()
    print("after calling Kazi()", x)

Moyeen()
print(x)
