def get_num(list1):
    
    num=[1,2,3,4,5,6,7,8,9]
    for x in list1:
        if x not in num:
        
            list1.remove(x)
    return list1

list1=["bhopal",25,"$","hello",43,'indore',22]
print("actual list is" ,list1)
print("list with numbers only")
print(get_num(list1))
