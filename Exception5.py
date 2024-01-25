''''''
'''
User Defined Exception
----------------------
- The exception defined by the user is known as "User defined exception".

- "raise" keyword / statement is used to generate user defined exception.
   It is used to raise exception forcefully for a particular condition.
 syntax:
        raise exception_name("Exceptio message")
'''
# try:
#     age = int(input('Enter your age:'))
#     if age < 0:
#         raise ValueError
#     print('Your age is ',age)
# except ValueError:
#     print('Age cannot be -ve')
#
# print('Rest of the code')
try:
    age = int(input('Enter your age:'))
    if age < 0:
        raise ValueError('Invalid age')
    print('Your age is ',age)
except ValueError as var:
    print('Age cannot be -ve',var)

print('Rest of the code')

'''
step 1: Create exception class and inherit it from base exception
        called "Exception"
     2: raise the exception message for the particular condition.
     
     3: raised exception can be handled using "except" block   
'''