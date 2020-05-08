def find_largest(*t):
    max=0
    large=''
    for x in t:
        if len(x)>max:
            max=len(x)
            large=x
    return x

print("the largest strin among them is  ",find_largest("january","feb","augusth"))
