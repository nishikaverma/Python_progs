import sys 
while True:
    
    try:
    
        a=int(input("enter an integer"))
        b=int(input("enter another integer"))
        c=a/b
        print("division is",c)

        break

    except(ZeroDivisionError,ValueError):
        x,y,z=sys.exc_info()
        print("error type",x)
        print("error message",y)
        print("error detailes",z)
        #print(sys.exc_info())
       
