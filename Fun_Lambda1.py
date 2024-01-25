''''''
'''
Lambda Function(Anonymous Function)
-----------------------------------
- These are the anonymous functions because they are not declared in the standard manner by using "def" keyword.

- We can use the "lambda" keyword to create small anonymous functions.

- These functions can take any no.of args. but return only one value in the form of an expression.

- Anonymous function cannot be a direct call to print because it requires an expression.

- Lambda functions have their own local namespaces and cannot be accessed other than those not in their parameter list and those in the global namespaces.

'''
add = lambda x,y : x+y

a = int(input('Enter 1st no:'))
b = int(input('Enter 2nd no:'))
res = add(a,b)
print(a, " + ", b , " = " ,res)





