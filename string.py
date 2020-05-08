str=input("enter a string")
i=0
while (str[i]!='\0'):
    if(str[i] in {"a","e","i","o","u"}):
        i+=1    
        continue
    else:
        print("%s\n"%str[i])
    i+=1    
