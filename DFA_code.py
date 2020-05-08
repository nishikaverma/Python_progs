 s=input("Enter a string of 0's and 1's : ")
i=0
count=1
l=len(s)

def q0(c):
    global i
    if i<l:
        if c==1:
            c=s[i+1]
            q1(c)
        if c==0:
            c = s[i + 1]
            q0(c)
    else:
        print("Cant reach the output, input string do not contains 3 consicutive 1's wrong!")
def q1(c):
    global i
    if i<l:
        if c==1:
            c=s[i+1]
            q2(c)
        if c==0:
            c = s[i + 1]
            q0(c)
    else:
        print("Cant reach the output, input string do not contains 3 consicutive 1's wrong!")
def q2(c):
    global i
    if i<l:
        if c==1:
            c=s[i+1]
            q3(c)
        if c==0:
            c = s[i + 1]
            q0(c)
    else:
        print("Cant reach the output, input string do not contains 3 consicutive 1's wrong!")
def q3(c):
    if c==1 or c==0:
        print("Congratulations! you reached to the final stage...your string has 3 consicutive 1's")

while i<l:
    if count==1:
        char=int(s[i])
        q0(char)

    count+=1