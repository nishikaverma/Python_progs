import sys 
while True:
    
    try:
    
        a=int(input("enter an integer"))
        b=int(input("enter another integer"))
        c=a/b
        print("division is",c)

        break

    except(ZeroDivisionError,ValueError) as e:
        print(e)
       
