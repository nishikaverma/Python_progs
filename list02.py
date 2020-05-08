an=input("enter an alphanumaric string")
mylist=[]
for x in an:
    if x in "0123456789":
        mylist.append(int(x))
        
print(mylist)
