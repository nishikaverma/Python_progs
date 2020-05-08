'''
PROBLEM STATMENT :-
Given an array A[]  of n elements. Your task is to complete the Function num which returns an integer denoting the total number of times digit k appears in the whole array.
For Example:
A[]={11,12,13,14,15}, k=1
Output=6 //Count of the digit 1 in the array'''



{
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        print(num(arr, n, k))


}

# Your task is to complete this function
# Function should return an integer
def num(arr, n, k):
    '''
    for x in arr:
        for i in str(x):
            if i==str(k):
                count+=1
    return (count)
    '''
    
    mylist=[x.count(str(k)) for x in map(str,arr) if str(k) in x ]
    return sum(mylist)