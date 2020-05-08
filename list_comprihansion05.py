

def flattern(list4):
    mylist=[y for x in list4 for y in x ]
    return mylist
    
i=0
list1=[]
while i<3:
    n=input("enter a no.")
    list1.append(n)
    i+=1
print("the list you entered is",list1)
i=0
list2=[]
while i<3:
    n=input("enter a no.")
    list2.append(n)
    i+=1

print("the list you entered is",list2)
i=0
list3=[]
while i<3:
    n=input("enter a no.")
    list3.append(n)
    i+=1
print("the list you entered is",list3)
list4=[list1,list2,list3]
print ("thevlist of all three list you enterde is",list4)
print("after calling flattern")
print(flattern(list4))
