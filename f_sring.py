#timeit.timeit(stmt,setup,timer,number)

import timeit

a=10
b=20
mystring="""print("the value if a is:",a,"value of b is",b,"and there sum is",a+b)"""
print(timeit.timeit(mystring,"import timeit"))

mystring="print('value of a is %d , value of b is %d and the sum is %d'(a,b,a+b))"
print(timeit.timeit(mystring,"import timeit"))

mystrin="print('the value of a is {0} ,b is{1} and there sum is{2}'.format(a,b,a+b))"
print(timeit.timeit(mystring,"import timeit"))

mystring="pprint(f'the value if a is {a} b is {b and sum is{a+b}}')"
print(timeit.timeit(mystring,"import timeit"))
