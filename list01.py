mylist1=[]
mylist2=[]
common_list=[]
n=1
while n<5:
    num=input("enter an integer:")
    if num in mylist1:
        print("value already present, enter a unique value")
    else:
        mylist1.append(num)
        n=n+1

print("integers inputted by you:")
for x in mylist1:
    print(x )

while n<5:
    num=input("enter an integer:")
    if num in mylist2:
        print("value already present, enter a unique value")
    else:
        mylist2.append(num)
        n=n+1

print("integers inputted by you:")
for x in mylist2:
    print(x )

for x in mylist1:
    if x in mylist2:
        common_list.append(x)

print("the common elements in both lists are:" common_list)
