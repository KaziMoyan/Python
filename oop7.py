"""


for row in range(7):
    for col in range(5):
        if col==0 or col==4 or (row==3 and (col >0 and col<4)):
            print("*",end="")
        else:
            print(end =" ")
    print()



for row in range(7):
    for col in range(5):
        if col==3 or ((row==0 or row==6)and col!=3):
            print("*",end="")
        else:
            print(end =" ")
    print()
"""
i =0
j=4
for row in range(7):
    for col in range(6):
        if col ==0 or (row == col+2 and col>1):
            print("*",end="")
        elif(row ==i and col ==j) and col>0:
            print("*",end="")
            i=i+1
            j=j-1
        else:
            print(end=" ")
    print()
