 
while True:
    
    try:
    
        a=int(input("enter an integer"))
        b=int(input("enter another integer"))
        
        if a<0 or b<0:
            raise Exception("negative no's not allowdwd.Try again!")
        
        c=a/b
        print("division is",c)
        break


        
    except ValueError:
        print("only integer values are excepted.Try again!")
    except ZeroDivisionError:
        print("denominator should not be zero.Please try again!")

    except Exception as e:
        print(e)
    
