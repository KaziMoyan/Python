f=open("p16 ","rt")
print(f.readline())
print(f.readlines())
content = f.read(354566)
for line in content:
    print(line)
print( content)

for line in f:
    print(line,end="")
    print(f.readline())

#content = f.read(344455)
#print("2", content)
f.close()

