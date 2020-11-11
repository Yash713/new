name="this is a simple task"

name=name.split()

newName=""

for i in range(0,len(name)):
    a=name[i]
    b=a[::-1]
    newName+=b
    newName+=" "
print(newName)
 
