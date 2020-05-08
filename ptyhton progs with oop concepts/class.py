class Animal:
    def __init__(self):
        self.age=19
        self.name='tommy'
        print("init() called ")
        print(type(self))
dog=Animal()
print("nmae",dog.name)
dog.breed='german shephard'
print("BREED IS",dog.breed)
print(dog)
print(type(dog))

