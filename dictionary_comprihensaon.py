
cars={"maruti":"ciaz","Hundai":"verna","honda":"amaze"}

# with dictonary comprihansion:
cars1={comp:car for (comp,car) in cars.items() }
print("original:",cars)
print("copyied:",cars1)

''' #without dictonary comprihansion(using copy() method):
cars1=cars.copy()
print(cars1) '''

'''#without using dictonary comprihansion or copy() method:
cares1={}
for (a,b) in cars.item():
    cars1[a]=b
print(cars1)'''
