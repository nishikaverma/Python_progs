# multithreading by making object if Thread class
import threading
def show():
    for i in range(10): # this is being executed by thread 1
        print("Ping")
        print("it is executed by :",threading.current_thread().getName())

t = threading.Thread(target=show)
t.start()
for i in range(10): # this is being executed by MainThread
    print("Pong")
    print("it is executed by :", threading.current_thread().getName())