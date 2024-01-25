''''''
'''
How to print the Exception name and Information about the Exception
-------------------------------------------------------------------
- To Print Exception name on output window we can use:
    1. exception class object
    2. using sys module
ex: using exception class object:
'''
n1 = int(input('Enter 1st no:'))
n2 = int(input('Enter 2nd no:'))

try:
    div = n1/n2
    print('Div : ',div)
except ZeroDivisionError as var:
    print('Error class is :',var.__class__)
    print('Erroe msg : ',var)

print('Rest of code')



