''''''
'''
 try block:
    - It contains the code that may generate exceptions.
 except[Exception_Name] block:
    - used to handle the exception(if exception occures)
 else:
    - used to execute the code if no exception arises.      
 finally block:
    - Always executed(with or without exception is arised),
       generally used in File handling cases. 

 - "else" and "finally" blocks are optional, we may/may not
    write them.
'''
a = int(input('Enter 1st no:'))
b = int(input('Enter 2nd no:'))

try:
    div = a/b
    print('Div : ',div)
except:
    print('Exception arised .. Plz try again')
else:
    print('No exception arised..')
finally:
    print('End of prog.')

print('Rest of the code..')


