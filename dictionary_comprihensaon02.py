mystr=str(input("enter a string"))
dict1={ k:mystr.count(k) for k in mystr}
for x,y in dict1.items():
    print(x,":",y)
