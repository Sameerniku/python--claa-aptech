'''
'''
'''
Implement of "Switch case"
-------------------------
- "switch" keyword doesnot exist in Python before version 3.10
 So alternate of switch case are for Python 3.9 or lower versions.
switch  case can be used :
    - By using Dictionary mapping
    - By using if-elif-else
    - match case(Python 3.10 onwords)
    
'''

# By using Dictionary mapping

def marks(name):
    mapping = {
        'Ram'   : 90,
        'Shyam' : 80,
        'Gopal' : 70,
        'Mohan' : 60
    }
    return mapping.get(name,'Student does not exist')

print(marks(input("Enter your name: ")))