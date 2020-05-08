def factorial(a):
    fact=1
    i=1
    while i<=a :
        fact=fact*i
        i+=1

    return fact

a=int (input("enter a no. for calculating ts factorial"))
b=factorial(a)
print(a,"!=",b)
