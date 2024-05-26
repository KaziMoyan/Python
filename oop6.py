
"""
rows= 6
for i in range (rows):
    for j in range (i):
        print (i , end= '')
    print('')

rows = 5
for i in range(1,rows +1):
    for j in range(1,i +1):
        print(j,end='')
    print('')

num = int(input("Enter your number :"))
for i in range (1,num+1):
    for j in range (1,i+1):
        print("*",end="")
    print()

num = int( input("Enter the number of rows:"))
k=1
for i in range(1,num+1):
    for j in range(1,k+1):
        print("1",end=" ")
    k=k+2
    print()

num = int(input("Enter the number of rows :"))
for i in range(0,num):
    for i in range(0,num-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()


num = int(input("Enter the number of rows :"))
for i in range (num, 0,-1):
    for j in range(0,num-i):
        print(end= " ")
    for j in range (0,i):
        print("*",end=" ")
    print( )


def pyramid(rows):
    for i in range(rows):
        print(''*(rows-i-1)+'* '*(i+1))
    for i in range(rows):
        print(''*(rows-j)+'* '*(j))


num  = int (input("Enter the numbers of rows:"))
for i in range(num,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()


for row in range (7):
    for col in range(5):
        if (col == 0 or col ==4) or ((row==0 or row== 3) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()


for row in range(7):
    for col in range(5):
        if (col==0 or col==4) or ((row==0 or row ==3 or row==6 ) and (col>0 and col<4)):
            print("*",end ="")
        else:
            print(end=" ")
    print()

for row in range(7):
    for col in range(5):
        if (col==0) or ((row==0 or row==6) and (col>0)):
            print("*",end="")
        else:
            print(end=" ")
    print()


for row in range(7):
    for col in range(5):
        if (col == 0) or (col == 4 and (row!=0 and row!=6 )) or ((row==0 or row==6)and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end =" ")


for row in range(7):
    for col in range(5):
        if (col==0) or ((row==0 or row==6) and (col>0)):
            print("*",end="")
        else:
            print(end=" ")
    print()

"""
str1="NAJEFA"
print_N= [[" " for i in range(6)] for j in range(6)]
print_A= [[" " for i in range(6)] for j in range(6)]
print_J= [[" " for i in range(6)] for j in range(6)]
print_E= [[" " for i in range(6)] for j in range(6)]
print_F= [[" " for i in range(6)] for j in range(6)]
print_A= [[" " for i in range(6)] for j in range(6)]
#for Code N
for row in range (6):
    for col in range(6):
        if col==0 or col==5 or (row == col and ( col>0 and col<5)):
            print_N[row][col]="*"

#For code A
for row in range (6):
    for col in range(5):
        if ((col==0 or col==4) and row!=0) or row==2 or (row==0 and(col!=0 and col!=4)):
            print_A[row][col]="*"

#for code J
for row in range (6):
    for  col in range (5):
        if (col==3) or (row== 5) and (col>0 and col<4) or (row==4 and col ==0) or(row==0):
            print_J[row][col]="*"
#for code E
for row in range (6):
    for  col in range (5):
        if col==0 or (row ==0 or row==3 or row==5) and (col>0):
            print_E[row][col] = "*"

#for F
for row in range (6):
    for  col in range (5):
        if col==0 or (row ==0 or row==3 or row==6) and (col>0):
            print_F[row][col] = "*"

#for A
for row in range (6):
    for col in range(5):
        if ((col==0 or col==4) and row!=0) or row==2 or (row==0 and(col!=0 and col!=4)):
            print_A[row][col]="*"



for i in range(6):
    for j in range(6):
       print(print_N[i][j],end=" ")
    print(end="  ")
    for j in range(6):
        print(print_A[i][j],end=" ")
    print(end=" ")
    for j in range(6):
        print(print_J[i][j],end=" ")
    print(end=" ")
    for j in range(6):
        print(print_E[i][j], end=" ")
    print(end=" ")
    for j in range(6):
        print(print_F[i][j], end=" ")
    print(end=" ")
    for j in range(6):
        print(print_A[i][j], end=" ")
    print()


