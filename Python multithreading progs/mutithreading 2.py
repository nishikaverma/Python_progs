# multithreading by making object if Thread class
import threading
def show():
    print(" after calling show i.e. inside show")
    print("executed by ",threading.current_thread().getName())


print("hello")
print("before calling show")
print("executed by",threading.current_thread().getName())
show()

t = threading.Thread(target=show) # making the obj of "Thread" class  ,
                                  # this line is also executed by 'MainThread' ,
                                  # "target" is a keyword arg. which only binds the function (here "show") with the object of Thread class (here "t") , this is similar to "bind()" function
                                  # here the control of function show () is handeled by another thread(created by us) whose default name is "Thread 1"
t.start() # function 'start()' is responsible for calling the function (here "show") whis is targetted by "target"
