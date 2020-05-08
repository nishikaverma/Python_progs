def find_largest(*s):
    i=0
    larg=1
    for j in s[i]:
        for j in range(1,s[i]):
            count=count+1
        i+=1
        if(count>large):
            large=count
    print("thv elargest string among ",s,"s ",large)

find_largest("nishi","samarth","father")
