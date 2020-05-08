mydict={1:"nishika", 2:"samrth",3:"mummy",4:"papa"}
print(mydict.get(3))
print(mydict.get(6))
print(mydict)
print(mydict[3])
for i in mydict:
    print("roll no. is",i)
for i in mydict.keys():
    print("roll:",i)

for roll in mydict.keys():
    print("roll  no is :",roll," and name is:",mydict[roll])

for roll,name in mydict.items():
    print("roll: ",roll,"name:", name)
