
"""


import pprint as pp
txt = 'This is a simple test from me'
letter= {}
for i in txt:
    letter.setdefault(i,0)
    letter[i] = letter[i]+1
pp.pprint(letter)


password_Bank = {'Moyeen': 123454,'Sumaiya':12345,'Nazifa':12345}
matched = False
x=0
print('Enter your name: ')

while x<5:
    name = input()
    if name in password_Bank:
        for i in range(0,3):
            print('enter your password:')
            password = input()
            if int(password) in password_Bank.values():
                matched = True
                print('Accsee Granted.')
                break
            else:
                print('Wrong Password.Enter Again : '+' you have '+str(2-i)+'tries = left')

    else:
        print('There is no such name is the password bank')
    if matched:
        break

Password_Bank = {'Moyeen':12345,'Sumaiya':1234,'Najifa': 234}
matched = False
x = 0
print('Enter your name : ')
while x<5:
    name = input()
    if name in password_Bank:
        for i in range(0,3):
            print('enter your password :')
            password = input()
            if int(password) in password_Bank.values():
                matched = True
                print('Access Granted.')
                break
            else:
                print('worng Password.Enter again :'+' you have  ' + str(2-i)+ 'tries = left')
    else:
        print('There is no such name in password bank:')
        if matched:
            break



contact_no = {'Moyeen':1234567,'Sumaiya':123123,'Najifa':989898}
x= 0
while x<5:
    print('Enter your name(press enter to exit): ')
    name = input()
    if name == '':
        break
    if name in contact_no:
        print('The contact number of ' +name +'is '+str(contact_no[name]))
    else:
        print("There is no such name in the phone book.")
        desc = input()
        if desc == 'yes':
            print('Enter the number :')
            num = input()
            contact_no[name]= num
            print('Dictionary Updated.')
        elif desc == 'no':
            print('Do u want to quite ')
            desc = input()
            if desc == 'yes':
                break
            else:
                print('Keep searching.')
    x= x+1

"""
identity = {'Name':'Ajwad','Age':'21','job':'Student'}
"""


#for i in identity.values():
    #print(i)
#for i in identity.keys():
    #print(i)
for i in identity.items():
    print(i)
    
x = list(identity.keys())
y = list(identity.values())
print(x)
print(y)

for k,v in identity.items():
    print('key:'+k+' value : '+v)
    

print('Name' in identity)
print('pop' in identity)

print ('11' in identity.values())
print('Age' in identity.keys())


print(str(identity.get('Name','defaullt')))
print(str(identity.get('height','Default')))

print(identity.setdefault('Name','Cosmos'))
print(identity.setdefault('Height','6ft'))
print(identity)


def sum_f(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum+i
    return sum
print(sum_f(6))
def sum_f2(n):
    if n == 0:
        return 0
    return n+sum_f2(n-1)
print(sum_f2(4))

def reverse_list(A):
    new_list = []
    for i in range (0,len(A)):
        new_list.append(0)
    for i in range( len(A)-1,-1,-1):
        print(new_list[len(A)-1-i])
        new_list[len(A)-1-i]=A[i]
    return new_list
list = [1,2,3,4,]
print(reverse_list(list))

def reverse_list_recursive(some_list):
    if len(some_list)==0:
        return []
    return [some_list[-1]]+ reverse_list_recursive(some_list[:-1])
print(reverse_list_recursive(list))


def fibo_recursive(n):
    if n<=1:
        return n
    return fibo_recursive(n-1)+ fibo_recursive(n-2)

print(fibo_recursive(4))



def exponent(x,y):
    if y == 0:
        return 1
    else:
        return x*exponent(x,y-1)
print(exponent(2,3))

def exponent(x,y):
    if y==0:
        return 1
    elif y % 2 == 0:
        return exponent(x,y//2)*exponent(x,y//2)
    else:
        return x*exponent(x,y//2)* exponent(x,y//2)
print(exponent(3,5))

"""




