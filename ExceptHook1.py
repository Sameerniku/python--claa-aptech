''''''
'''
 ExceptHook in Python
 --------------------
 - It is used to modify the "Trace back" msg which arises when error occures
   generally.
 - As per the example if we want to add(+) num with String then a "TypeError"
   will arise.   
 - What happens when we donot write the suspecious code with in try block:
    - The interpreter internally calls the sys.exception() method
      with 3 args.
          i.  exception class
         ii.  exception instance/value
        iii.  A trace back object  
 - The function then prints out a given traceback and exception to the 
    sys.stderr(output screen)
 - Inside the sys module excepthook is defined :
    def excepthook(exc_type,exc_value,exc_traceback):
        #print arguments    
  - We can override this definition. 
     sys.excepthook() handles the uncaught exceptions.  

'''
# def add1():
#     print(10+'Good Evening')
#
# add1()

import sys
def format_traceback(exc_type,exc_value,exc_traceback):
    print('Some thing went wrong')
    print(exc_type)
    print(exc_value)
    print(exc_traceback)

sys.excepthook = format_traceback # giving new defenition to excepthook

def display():
    print(10 + 'Good Evening')

display()