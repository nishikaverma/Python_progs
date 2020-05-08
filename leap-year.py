y=int(input("eter a year"))
if(y%4==0):
    if(y%100!=0):
        print("%d is a leap year "%y)
    else:
        print("%d is not a leap year "%y)
else:
    print("%d is not a leap year "%y)
