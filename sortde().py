mylist=[]
n=1
while n<6:
    num=input("enter an integer")
    mylist.append(num)
    n=n+1

print("the list you entered is", mylist)

i=0
l=len(mylist)
while i<l:
    j=i
    while j<l:
    
        if mylist[j]>mylist[j+1]:
            mylist[i],mylist[j]=mylist[j],mylist[i]
        j+=1
    i+=1



print("the sorted list is",mylist)
