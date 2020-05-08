# Multithreading by  extending thread class:
from threading import *
class MYthread(Thread):
    def run(self): # as run is an empty body function inside the class "Thread"
        for i in range(10):
            print("Ping")

t =MYthread()
t.start() # this line will immediately call the function run()
for i in range(10):
    print("Pong")
