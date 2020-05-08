#timeit.timeit(stmt,setup,timer,number)

import timeit

a=10
b=20
mystring="""print("the value if a is:",a,"value of b is",b,"and there sum is",a+b)"""
x=timeit.timeit(mystring)
print(x)
mystring="print('value of a is %d , value of b is %d and the sum is %d'(a,b,a+b))"
y=timeit.timeit(mystring)
print(y)

mystrin="print('the value of a is {0} ,b is{1} and there sum is{2}'.format(a,b,a+b))"
z=timeit.timeit(mystring)
print(z)

mystring='print(f"the value if a is {a} b is {b} and sum is{a+b}")'
c=timeit.timeit(mystring)
print(c)
