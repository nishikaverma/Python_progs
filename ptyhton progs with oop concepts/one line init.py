class emp():
    def __init__(self,**kwargs):
        self.__dict__.update(kwargs)
    def show(self):
        print(self.__dict__)
E=emp(age=68,name="satish",sal=50000.0)
E.show()
