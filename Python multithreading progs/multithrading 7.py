# Multithreading by  extending thread class:
import time
from threading import *

class square(Thread):
    def __init__(self,nos):
        Thread.__init__(self)
        self.nos=nos

    def run(self):
        for i in self.nos:
            print("sq. is",i*i)
            time.sleep(1)

class cube(Thread):
    def __init__(self, nos):
        Thread.__init__(self)
        self.nos = nos

    def run(self):
        for i in self.nos:
            print("cube. is",i*i*i)
            time.sleep(1)

x= time.time()
mynos=[1,2,3,4,5,6]
t1=square(mynos)
t2=cube(mynos)
t1.start()
t2.start()
t1.join()
t2.join()
y=time.time()
print("total time taken by script :",y-x,"sec")