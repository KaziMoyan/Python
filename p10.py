"""list1 =  [ ["Moyeen",1],["larry",6],["Karri",5],["Marie",9]]
#print(list1)
#print(list1[0])
dict1= dict(list1)
for item in dict1:
    print(item)
print(dict1)

for item,lolopop in list1:
    print(item,"Lolipop",lolopop)

items = [int, float, "Moyeen", 4,5,67,7,34,3,3,54]
for item in items:
 if str(item).isnumeric() and item:
   print(item)

items = [int, float, "HaERRY", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]

for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)

i =0
while(i<45):
    print(i)
    i = i +1
i = 0
while (i < 45):
    print(i +1 ,end =" ")
    i = i + 1

i = 0
while (True):
    print(i+1, end=" ")
    if(i==44):
        break
        i=i+1

i = 0
while (True):
    if i + 1<5 :
      i=i + 1
        continue
    print(i+1, end="")
    if(i==44):
           break
    i=i+1

while(True):
    inp = int(input("Enter a number :"))
    if inp>100:
        print("Happy birthday to u ")
        break
    else:
        print("This is not your perfect age ")
        continu

"""
print("Enter 1st Number")
num1 = int(input())
print('Enter 2nd Number')
num2 = int(input())
print('so What you Want?'+'+,-,/,%,*')
num3 =input()

if num1 ==45 and num2==3 and num3=='*':
    print("555")
elif num1 == 56 and num2 == 9 and num3 == '+':
        print("77")
elif num1 == 56 and num2 == 6 and num3 == '/':
        print("4")
elif num3=='*' :
    num4=num1*num2
    print(num4)
elif num3 == '+':
    plus=num2+num1
    print(plus)
elif num3 == '/':
    Dev=num2/num1
    print(Dev)
elif num3 == '-':
    Dev=num2-num1
    print(Dev)
elif num3 == '%':
    percent=num2%num1
    print(percent)
else:
    print("Error! Please check your input")