dict1={"a":1,"b":2,"c":3,"d":4,"e":5}
dict_new={k:v*v for (k,v) in dict1.items()}
print(dict_new)
