m=0
for i in range(4):
    m+=1
    for i in range(m): 
        print("*",end=" ") 
    print("\n")

#code for reverse of above series:
for i in range(5,1,-1):
    for j in range(1,i-1):
        print("*",end=" ")
    print("\n")
