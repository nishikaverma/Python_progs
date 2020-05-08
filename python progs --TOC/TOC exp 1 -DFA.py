#############################################################################
# A DFA which accepts input sring of {0,1} which contains 3 consicutive 1's #
#############################################################################

def validate(s):
    if len(s)>0:
        for x in s:
            #print(type(x))
            if x!='0' and x!='1':
                print("Invalid string! The string should only contain 0's and 1's ")
                break
        q0()

def q0():
    global count 
    #print("in q1",count)
    if count<len(s):
        if s[count]=='1':
            count+=1
            q1()
        elif s[count]=='0':
            count+=1
            q0()
    else:
        print("Invalid string!")
    
    
def q1():
    global count
    #print("in q1",count)
    if count<len(s):
        if s[count]=='1':
            count+=1
            q2()
        elif s[count]=='0':
            count+=1
            q0()
    else:
        print("Invalid string! ")
        
def q2():
    
    global count
    #print("in q2",count)
    if count<len(s):
        if s[count]=='1':
            count+=1
            q3()
        elif s[count]=='0':
            count+=1
            q0()
    else:
        print("Invalid string! ")

def q3():
    global count
    global got_result
    #print("in q3",count)
    if count<len(s):
        if s[count]=='1' or s[count]=='0':
            count+=1
            q3()
    if count==len(s):
        if got_result==0: 
            print("Input accepted!")
            got_result=1

s=input("Input any string of 0's and 1's to DFA : ")
count=0
got_result=0 #for preventing the output to come multiple times, if the string contains '111' multiple times.
validate(s)
