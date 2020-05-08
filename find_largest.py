def find_largest(*s):
    count=0
    for i in s:
       if len(i)>count:
           count=len(i)
           name=i
    print("largest string is '",name," ' with length=",count)

find_largest("nishi","samarth","bhpoal","i dont know!!")
