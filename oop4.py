"""
x= 0
while x<5:
    print (x)
    x= x+1



for i in range (20,-10,-3):
    print(i)

while True:
        print('Please enter your name:')
        name = input()
        if name == 'your name':
            break

print('over')

while True:
    print('What is your name :')
    name = input()
    if name != 'Batman':
        continue
    print('hello there ' +name+ '.what is the passcode ?')
    passcode = input()
    if passcode == "ice":
        break
    print('al-right')

sum = 0
for i in range(2,10) :
    sum = sum + i
print(sum)

sum=0
for i in range (1,6):
    sum = sum+i*i
print(sum)

odd_sum =0
for i in range(1,10,2):
    odd_sum = odd_sum+i

print(odd_sum)

even_sum =0
for i in range(2,10,2):
    even_sum = even_sum+i

print(even_sum
"""
sum = 0
for i in range(1,5):
    for j in range(1,i+1):
        sum = sum+j
print(sum)

