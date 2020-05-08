ch=input("enter something")
c=ch[0]
if("A"<=c<="Z"):
    print('%s is a capital letter'%c)
elif("a"<=c<="z"):
    print('%s is not is capital letter '%c)
elif("0"<=c<="9"):
    print('it is a digit')
else:
    print('it is a special symbole')
