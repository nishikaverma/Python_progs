
# multithreading by making object if Thread class
import threading
def show1(): # execution handeleled by Thread 1
    for i in range(10):
        print("good")
        print("this execution is handeled by",threading.current_thread().getName())

def show2():  # execution handeleled by Thread 2
    for i in range(10):
        print("morning")
        print("this execution is handeled by", threading.current_thread().getName())
def show3():  # execution handeleled by Thread 3
    for i in range(10):
        print("user")
        print("this execution is handeled by", threading.current_thread().getName())

t1 = threading.Thread(target=show1)
t2 = threading.Thread(target=show2)
t3 = threading.Thread(target=show3)
t1.start()
t2.start()
t3.start()

# the messages are not in sequential order because the execution time of diffrent threads may vary
