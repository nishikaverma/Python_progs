def  find_largest(*s):
    i=0
    while i<=len(s):
        for j in s[i]:
            for j in range(1,len(s[i])):
                count=count+1
            i+=1
            if(count>larg):
                larg=count
        print("thv elargest string among ",s,"s ",large)


find_largest("nishi","samarth","father")
