def get_len(string):
    mylist=[len(x) for x in string.split() if x!="the" ]
    return mylist
string=input("ente a string")
print(get_len(string))
