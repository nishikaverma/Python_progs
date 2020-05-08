num=int(input('enter a no. '))
fact=1
for i in range(1,num):
    fact=fact*i
fact=fact*num
print("{}!= {}".format(num,fact))
