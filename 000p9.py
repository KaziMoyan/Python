+-0
"""
a=[1,2,3,4,5]
b=['a','b','c','d']
z=[3.1416,'pi',23]
#print(z)
print(a[3])


x=[[1,2,3],[4,5,6]]
print(x[0][2])


p=[1,2,3,4,5]
print(p[-1])
print(p[-2])


q = [1,2,3,4,5,6]
print(q[0:5])
print(q[1:4])
print(q[0:-2])
print(q[1:-1])
print(q[:4])
print(q[0:5])

a=[1,2,3,4,5]
b=['x','y','z']
ab=a+b
print(ab)
xx=['p','q','r']
new_x=xx*2
print(new_x)


p=['a',0,9]
del p[1]
print(p)



places_visited = ['Rasa','india','Nepal','Malaysia','babtan','usa','bae']
#print(places_visited.index('bhutan'))
#places_visited.append('Africa')
#print(places_visited)

#places_visited.insert(2,'uk')
#print(places_visited)
#places_visited.remove('Nepal')
#print(places_visited)
#places_visited.sort()
print(places_visited)
places_visited.sort(key=str.lower,reverse=True)
print(places_visited)
"""
#tup = (1,2,3,'hello',9.88)
#print(tup)
#print(type(tup))
#print(tup[4])
#print(tup[:3])
#new_list = list(tup)
#print(new_list)
#print(type(new_list))
#T = tuple(new_list)
#print(T)
#print(type(T))\
import copy as cp
def f(some_list):

    some_list.append('ok')

x= [1,2,3]
s = cp.copy(x)
cp.deepcopy()
f(s)
print(x)





