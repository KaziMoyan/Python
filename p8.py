s = set()
#print(type(s))
#l = [1,2,3,4,5]
#s_from_list = set (l)
#print(s_from_list)
#print(type(s_from_list))
s.add(1)
s.add(4)
s1 = s.intersection({1,2,3,45})
print(s,s1)
print(len(s))
s1 =s.isdisjoint(s1)
print(s1)
s.remove(1)


