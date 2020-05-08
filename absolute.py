def absolute(a):
    if(a<0):
        b=a+(-a)
        b=b+a
        return b
    if a ==0:
        return a
x=absolute(10)
print("absolute value of 10 is",x)
x=absolute(-10)
print("absolute value of -10 is",x)

x=absolute(0)
print("absolute value of 0 is",x)
