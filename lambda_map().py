
names=["january","feb","march"]
print(list(map(lambda string: "EVEN" if len(string)%2==0 else string[0],names)))
