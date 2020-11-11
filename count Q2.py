a=str(input("enter here"))
dict={}
for i in range(len(a)):
    dict[a[i]]=a.count(a[i])
print(dict)

count1=0
count2=0
for i in a:
     if(i.isdigit()):
         count1+=1
     count2+=1
print("the number of digits are : ")
print(count1)

print("the number of alphabets are : ")
print(count2)
