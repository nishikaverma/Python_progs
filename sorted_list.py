
mylist=[]
n=1
while n<=5:
    num=int(input("enter a no."))
    pos=0
    for x in mylist:
        if num>x:
            break
        pos+=1
    mylist.insert(pos,num)
    n+=1

print("the sorted list is",mylist)
