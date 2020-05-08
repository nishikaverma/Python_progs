import traceback
while True:
    
    try:
    
        a=int(input("enter an integer"))
        b=int(input("enter another integer"))
        c=a/b
        print("division is",c)

        break

    except(ZeroDivisionError,ValueError):
        print(traceback.format_exc())
       

