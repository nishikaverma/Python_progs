
name=input("enter name")
l=len(name)
print("last charactor of ur name is",(lambda str:str[l-1])(name))

#2nd way of coad

n=lambda str:str[len(str)-1]
print("the last charsctor of ur name is",n("nishika"))
