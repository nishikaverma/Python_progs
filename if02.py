a,b,c=input("enter three no's [seprated by space]").split
a=int(a)
b=int(b)
c=int(c)
if(a>b):
    if(a>c):
        print('a=%d is greatest no.'%a)
        
if(b>a):
    if(b>c):
        print('b=%d is greatest no.'%b)

if(c>a):
    if(c>b):
        print('c=%d is greatest no.'%c)
