li=list(int(x) for x in input('Enter some number:') )
sum_list=[]
print(li)

# complexity is = n(n-1)

############################
for i in range(0,len(li)):
    pro=1

    for  j in range(0,len(li)):

        if j!=i:
            pro=pro*li[j]

    sum_list.append(pro)
    
#############################    

print(sum_list)
