''''''
'''
   FUNCTION
   --------
- A function is a block of organized, reusable code used to perform
  a particular task.

- Functions provide better modularity for the application and high
  degree of code reusability.
  
- Python gives many built-in functions like print(), input() etc.
  also we can create user defined functions.  

  Defining a Function
  -------------------
- keyword "def" is used to define a function.

- Parameters are passed inside the paranthesis of the function name.

- Function body should be written using indentation for identification of
  function block.

- "return" statement indicates the end of the function definition.
   if returns nothing then we can write, " return None "
   
 syntax:
        def fun_name(arg_list):
             -----------
             ----body---  
            return statement
      
'''
def sum(a,b):
    res = a+b
    return res

x = int(input('Enter 1st no.:'))
y = int(input('Enter 2nd no.:'))
print('Calling sum function by passing the args')
print('Addition is ',sum(x,y))


