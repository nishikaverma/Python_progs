def get_upper(string):
    mylist=[x for x in string if 65<=ord(x)<=90 if x not in 'AEIOU']

    return mylist
string=input("enter a string")
print(get_upper(string))
