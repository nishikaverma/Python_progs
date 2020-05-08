mylist1=[]
mylist2=[]
common_list=[]
# inputting values in 1st list:
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

# inputting values in 2nd list:
n=1
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

# searching for common elements:
for x in mylist1:
    if x in mylist2:
        common_list.append(x)
        
#printing common elements :
        
if len(common_list)==0:
    print("no common elements in both list")
else:

    print("the common elements in both lists are:", common_list)
