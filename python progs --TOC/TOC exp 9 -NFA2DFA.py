
# NFAstates = number of states in NFA
# total_Ip_alp = number of input alphabts 
# input_alphabets= list of all ip alphabets
# q =  dictionary for each state , contains i/p alphabet as keys and list of transition state at that i/p as values.
# NFAstate_transition = list of dictionaries of weach state

import HTML

print("NOTE :-- ALWAYS ENTER 'N' FOR NULL TRANSITION \n   Enter multiple transition states as a list \n -------------------------------------")


#------------- taking  NFA input --------------------------

NFAstates = int(input("Number of states in NFA : "))

total_Ip_alp = int(input("Number of input alphabets : "))
input_alphabets=[]
for i in range(total_Ip_alp):
    input_alphabets.append(input(" i/p alphabet : "))

NFAstate_transition =[]
for s in range(NFAstates):
    q={}
    print("transition at q",s," state :")
    for ip in input_alphabets:
        print("For ",ip," : ")
        q[ip]=input()
    
    NFAstate_transition.append(q)

print (NFAstate_transition)

#-----------------------------------------------------------

t = HTML.Table(header_row=input_alphabets)
for x in range(NFAstates):
    lst=[]
    for i in input_alphabets:
        lst.append(list(NFAstate_transition[x][i]))

    t.row.append(lst )

print(t)



