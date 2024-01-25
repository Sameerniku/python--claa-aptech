''''''
'''
Exception:
----------
- It is the event which occures during the execution of the program that
  disrupts normal flow of the program.
- It's a situation that Python compiler cannot adjust/resolve it.  
  ex: zeroDivision error

What happens when Exception arises:
    - Leads to sudden termination of the program
    - can block the application
    - data loss may arise
    - corrupt the files 
      etc.  
- Diff. between Error & Exception is,
        - errors cannot be handled, it should be rectified first otherwise
          program will be terminated.
        - exceptions can be handled using exception handling mechanism
          which avoids abnormal termination of the program.  
  
-  Exceptions can be handled by using 4 keywords,
          i - try    block
         ii - except  "
        iii - else    "
         iv - finally " 
   
     
'''

a = int(input('Enter 1st no:'))
b = int(input('Enter 2nd no:'))
res = a/b
print('Div = ',res)