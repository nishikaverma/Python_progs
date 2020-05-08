dict1={"a":1,"b":2,"c":3,"d":4,"e":5}
new_dict={k:v for  (k,v) in dict1.items() if v>2 and v%2==0}
print(new_dict)
