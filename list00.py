mylist=[]
n=1
sum=0
while n<6:
    num=input("enter %d number"%n)
    mylist.append(num)
    sum=sum+int(mylist[n-1])
    n=n+1

print("the list is:")
for x in mylist:
    print(x)
print("the sum is:",sum )
    
