def inspect(string):
    if len(string)%2==0:
        return "EVEN"
    else:
        return string[0]

names=["nishika","hbopal","karachi","indore"]
print(list(map(inspect,names)))
