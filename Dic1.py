my_stuff = {'book':'cookBook','phone' : 'iPhone','home':'Bd'}
print(my_stuff['book'])
#print(my_stuff['cookBook'])
x = {0:100,1: 200,3:300,4:500}
print(x[4])
a= [1,2,3]
b= [3,2,1]
print(a==b)
c={1:100,2:200}
d={2:200,1:100}
print(c==d)
D={'a':100,'b':200}
DE={'a':300,'b':400}
new_dic = D.copy()
new_dic.update(DE)
print(new_dic)