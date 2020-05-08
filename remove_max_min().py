def remove_max_min(list1):
    mylist=[x for x in list1 if x!=min(list1) and x!=max(list1)]
    return mylist

list1=list(input("enter a sequence of num."))
print("the original list is",list1)
print("list after removing the max and min values is")
print(remove_max_min(list1))
