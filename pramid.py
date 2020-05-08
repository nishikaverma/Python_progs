a=['*','*','*','*']
for i in a:
    for i in a[:3]:
        print(i,end=" ")
    print("\n")


#the second way of writting this code{less complex}

for i in range(1,5):
    for i in range(1,4):
        print("*",end=" ")
    print("\n")

# the same code using a single for loop
for i in range(1,5):
    print("*  "*3)
