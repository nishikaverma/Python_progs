while True:
    
    try:
    
        a=int(input("enter an integer"))
        b=int(input("enter another integer"))
        c=a/b
    except ZeroDivisionError:
        print("please enter a non zero denominator!")
        

    except ValueError: 

        print("please enter only integer value!")

    else:
        c=a/b
        print("division is",c)

        break
