"""def search(List, n):
    for i in range (len(list)):
        if List[i]==n:
            return True
    return False
List=[1,2,'sachin',4,'Geeks',6]
n = 'Geeks'
if search(List,n):
    print("found")
else:
    print("Not found")

 Sum
def sum_list(items):
    sum_numbers =0
    for x in items:
        sum_numbers +=x
    return sum_numbers
print(sum_list([1,2,3,4,5]))


def multiply_List(items):
    multyply_numbers =1
    for x in items:
        multyply_numbers *= x
    return multyply_numbers
print(multiply_List([1,2,3,4,5]))


def max_num_in_list(list):
    max = list[4]
    for a in list:
        if a> max:
            max = a
    return max
print(max_num_in_list([1,2,3,4,5]))


def max_num_in_List(list):
    max = list[4]
    for a in list:
        if a>max:
            max = a
    return max
print(max_num_in_list())


def max_num_in_list(List):
    min = List[0]
    for a in List:
        if a< min:
            min=a
    return min
print(max_num_in_list([6,2,3,4,5]))


def match_words(words):
    ctr = 0
    for word in words:
        if len(word) >1 and word[0] == word[-1]:
            ctr +=1
    return ctr
print(match_words(['abc','xyz','aba','1221']))


def last(n):
    return n[-1]
def sort_list_last(Tuples):
    return sorted(Tuples, key=last)
print(sort_list_last([(2, 5), (1, 0), (4, 9), (1, 1), (1, 4)]))


a = [10,23,33,44,10,44,55,58,55,11,99,11]

dump_items = set()
#uniq_items = []
for x in a :
    if x not in dump_items:
        #uniq_items.append(x)
        dump_items.add(x)
print(dump_items)



i = {1, 2, 3}
if not []:
    print("list is empty ")
else:
     print('not empty')



original_list = [10,11,22,3,44]
new_list = list(original_list)
print(original_list)
print(new_list)


def long_words(n,str):
    word_len =[]
    txt = str.split(" ")
    for x in txt:
        if len(x)>n:
            word_len.append(x)
        return word_len
print(long_words(3,"fhwerfuiergfeorfgffffffff rfrrrrrrr"))


color = ['red','green','white','black','pink','yellow']
color= [x for (i,x) in enumerate(color)if i not in(0,4,5)]
print(color)


array=[[['1' for col in range(6)] for col in range(6)] for row in range(3)]
print(array)


num = [7,10,11,44,55,6677,22,33,44]
num = [x for x in num if x%2!=0]
print(num)

def printValues():
    l = list()
    for i in range(1,21):
        l.append(i**2)
    print(l[:5])
    print(l[-5:])
printValues()

def printValues():
    l = list()
    for i in range(1,31):
        l.append(i**2)
        print(l[5:])
printValues()


import itertools
print(list(itertools.permutations([1,2,3])))


list1 = [1,2,3,4,5]
list2 = [2,3,4,5,6]
diff_list1_list2 = list(set(list1) - set(list2))
diff_list2_list1 = list(set(list2) - set(list1))
total_diff = diff_list2_list1 + diff_list2_list1
print(total_diff)

s = ['a','b','c','d']
str1 = ' '.join(s)
print(str1)

fav_movie = []
while True:
    print('movie no'+str(len(fav_movie)+1)+ 'or press Eneter to stop adding')
    movie = input()
    if movie == '':
        break
    fav_movie = fav_movie + [movie]
if len(fav_movie)!=0:
    print('the lists are ')
    for i in range(len(fav_movie)):
        print(fav_movie[i])

fav_movie = []

my_tech = ['iphone','android','Asus Laptop','monitor']
print('Enter your name:')
name = input()
if name not in  my_tech:
    print('nope its not in the list')
else:
    print(name+'is my tech')



chocolate_milk_shake = ['chocolate','milk','ice_cream','blender']
x,y,z,q = chocolate_milk_shake
print(x,y,z,q)


a="whtas a list now "
print(a[0])

"""

