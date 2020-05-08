def removevowels(string):
    mylist=[]
    vowels=["a",'e','i','o','u']
    for x in string:
        
        if x not in vowels:
                
            mylist.append(x)
            
    return mylist
    
string=input("enter a string")
print(removevowels(string))


    
