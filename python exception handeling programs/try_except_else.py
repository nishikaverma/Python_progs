while True:
    
    try:
    
        a=int(input("enter an integer"))
        b=int(input("enter another integer"))
        c=a/b
         print("division is",c)

        break

    except(ZeroDivisionError,ValueError):
        print("denominator should be non zero and only integer inptuts are allowded.Please try again!")
        

       
