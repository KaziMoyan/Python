

""" 
file = open('oop8.csv')
file_reader = csv.reader(file)
#print(file_reader)
data = list(file_reader)
print(data)
print(data[0][2])
for row in file_reader:
    print('row no = '+str(file_reader.line_num)+' '+str(row))


output_file = open('ooop10.py.csv','w',newline=' ')
output_writer= csv.writer(output_file,delimiter=".")
output_writer.writerow(['1','2','3','4'])
output_writer.writerow(['14','25','36','47'])
output_file.close()



f = open('a.txt','w')
print(f.name)
print('is it closed ',f.closed)
print('mode=',f.mode)
f.write('nowadays python is my fav language ')
f.close()

f = open('a.txt','a')
f.write('i also love java')
f.close()

f = open('a.txt','r+')
info = f.read(12)
print(info)

f = open('a.txt','w')
f.write("all is lost ")
"""
""" 

#open#
f = open('ab.txt','w')

print('name =',f.name)
print('is it close :',f.closed)
print('mode :',f.mode)
f.write('python is my favorite language.')
f.close()

#appending#

f = open('ab.txt','a')
f.write('i also love java')
f.close()

#read+ ##

f = open('ab.txt','r+')
info = f.read(20)
print(info)
f.close()

#open#
f = open('ab.txt','w')
f.write('all is lost')
f.close()

"""


