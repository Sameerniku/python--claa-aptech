''''''
'''
Built-in functions
---------------------
getattr(obj_name,attribute_name)
    - It returns the value assigned to the attribute.

setattr(obj_name,attribute_name)
    - It sets a new value to the attribute.    

delattr(obj_name,attribute_name)
    - It deletes an attribute.
    
hasattr(obj_name,attribute_name)
    - It checks whether an attribute is present or not.(True / False)

Built in Attributes
-------------------
__dict__ :- Dictionary containing the class's namespace.

__doc__ :- Class documentation/ purpose of th class in  string.

__name__ :- Name of the class

__module__  :- Module name in which class is defined.

__base__ :- List of base classes (used in inheritance)


isinstance() function:-  It returns "True" if the object is 
   specified types and it will not match then return "False".
   syntax:
      isinstance(obj,class) 

'''
class Employee:

    def __init__(self,n,a):
        self.name = n
        self.age  = a

    def display(self):
        print('Name : ',self.name)
        print('Age  : ', self.age)

e1 = Employee('RAM',21)
e2 = Employee('SHYAM',22)


e1.display()
e2.display()

print(getattr(e1,'name'))
print(setattr(e1,'name','RAM NARAYAN'))
print(getattr(e1,'name'))
print(e1.__dict__)
print('Age in e2 is available ? : ',hasattr(e2,'age')) # False

delattr(e2,'age')
print(e2.__dict__)

print('Name in e1 is available ? : ',hasattr(e1,'name')) # True
print('Age in e2 is available ? : ',hasattr(e2,'age')) # False

print(isinstance(e1,Employee))
print(isinstance(e2,Employee))


