import threading
def show():
    print("inside show")
    print("executed by ",t1.getName())


print("hello")
t1=threading.current_thread()
print("executed by",t1.getName())
show()


# thus here multithreading is not done  as the program is handeled by a single thread called a "MainThread"

