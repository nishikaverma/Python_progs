inp=input("enter 5 inegers")
mylist=[]
sum=0
for x in inp.split():
    mylist.append(int(x))
    sum=sum +int(x)
print("list is ",mylist)
print("sum is",sum)
