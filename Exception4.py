''''''
'''
2. using "sys" module
ex:
'''
import sys
n1 = int(input('Enter 1st no:'))
n2 = int(input('Enter 2nd no:'))

try:
    div = n1/n2
    print('Div : ',div)
except ZeroDivisionError as var:
    print(sys.exc_info()[0]) # Exception class name
    print(sys.exc_info()[1]) # Info about the exception

print('Rest of code')
'''
- Multiple errors can also occur but the message will arise for the
  1st exception which arised first, as the control doesnot move to the
  next line  until the current line exception is resolved. 

'''
