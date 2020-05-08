
num= list( input("Enter integer" )for x in range(10))
even=sum(map(int,num[0::2]))
odd=sum(map(int,num[1::2]))
print("the output is",abs(even-odd))



