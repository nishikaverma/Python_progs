class GreaterThan10Exception(Exception):
    pass
class NegativeNumberException(Exception):
    pass
while True:
    
    try:
    
        a=int(input("enter an integer"))
        b=int(input("enter another integer"))
        c=a/b
        if a<0 or b<0:
            raise  NegativeNumberException("negative numbers not allowded.Try again!")
        if b>10:
            raise GreaterThan10Exception("denominator should not be greater than 10.Try again!")
        print("division is",c)

        break

    except ZeroDivisionError:
        print("please enter a non zero denominator!")
        

    except ValueError: 

        print("please enter only integer value!")

    except GreaterThan10Exception as e:
        print(e)
    except NegativeNumberException as e:
        print(e)
       
