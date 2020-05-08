def greatest_no(lst):
    greatest=0
    for i in range(len(lst)-1):
        if lst[i]>greatest:
            greatest=lst[i]
        
    return greatest
n=int(input("How many no's. you want to enter? : "))
lst=[]
print("enter ",n," numbers :")
[lst.append(int(input())) for i in range(n) ] 
print("list : ",lst)
print("greatest is ",greatest_no(lst))
