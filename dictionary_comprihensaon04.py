dict1={"a":1,"b":2,"c":3,"d":4,"e":5}
dict2={k:"even" if v %2==0 else "odd" for (k,v) in dict1.items()}
print(dict2)
