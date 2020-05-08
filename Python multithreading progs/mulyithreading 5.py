# multithreading by making object if Thread class
import time
import  threading
def square(nos):
    for i in nos:
        print("sq. is",i*i)
        time.sleep(1) # method "sleep()" of module "time " pauses the thread for 't' seconds (which is given as an argument to it)

def cube(nos):
    for i in nos:
        print("cube. is",i*i*i)
        time.sleep(1)


print("total threads in action at starting :",threading.active_count())
x= time.time() # method "time()" of module "time " gives the current time period
mynos=[1,2,3,4,5,6]
t1=threading.Thread(target=square,args=(mynos,))
t2=threading.Thread(target=cube,args=(mynos,))
print("total threads in action when t1 is started:",threading.active_count())
t1.start()
print("total threads in action after t2 has started :",threading.active_count())
t2.start()
print("total threads in action when mainThread is slept :",threading.active_count())
t1.join() # function of "join" :- if thread t1 is running ,the 'join' stops the thread from which the thread t1 is called (here it stops the Mainthread)until the execution of t1 is over

print("total threads in action when mainThread is slept:",threading.active_count())
t2.join()
print("total threads in action after t1 and t2 are dead:",threading.active_count())
y=time.time()
print("total time taken by script :",y-x,"sec")