''''''
import threading

'''
    Exception in Multithreading
    ---------------------------
 - In multithreading multiple threads are running simultaneously.
 - When exception occures in one thread, it will not disturb other 
   threads.    
 - When exception arises in thread:
        - The interpreter calls "threading.exceptionhook()" with one 
          argument(i.e. named tuple with 4 args)
          i. exception class
         ii. exception instance/value
         iii. traceback object
         iv.  Thread name
 - In case of general exception the interpreter calls the "sys" module,
   where as in case of exception in multithreading it calls the specially 
   defined "threading.exceptionhook()" method            
'''
from threading import *
from time import sleep

def custom_hook(args):
    print('Exception occured in Thread')
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])

def display():
    for i in range(5):
        sleep(2)
        print("Hi" + "Good Evening")
        # print("Hi"+ 10) # will generate exception
def show():
    for i in range(5):
        print("Hello")
        sleep(0.5)

threading.excepthook = custom_hook
t1 = Thread(target=display)
t2 = Thread(target=show)

t1.start()
t2.start()
t1.join()
t2.join()

for i in range(5):
    print("Bye")

