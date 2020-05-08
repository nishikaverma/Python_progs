
def compute(n1,n2):
    if n1>n2:
        smaller=n2
    else:
        smaller=n1
    for i in range(1,smaller+1):
        if (n1 % i==0 ) and (n2 % i==0):
            gcd=i
    return gcd



n1,n2=map(int,input("enter 2 numbers : ").split())
print("The GCD of ",n1," and ",n2," is : ",compute(n1,n2))  