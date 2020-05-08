sum=0
while(1):
    num=int(input("enter a no.{enter 0  to stop insertion}"))
    if(num==0):
        print("{end of the loop}\n")
        break
    if(num<0):
        continue
    sum=sum+num

print("the sum of no.'s you entered is %d"%sum)
