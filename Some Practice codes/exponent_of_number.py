def exp(n,e):
    
    # Way 1 :- general sol. 
    '''
    result = n**e
    return result
    '''
    #Way 2 : Using recursion
    if e==1:
        return n
    else:
        return(n*exp(n,e-1))

n,e=map(int,input("Enter a number and its exponent you want : ").split())
print("Result : ",exp(n,e))