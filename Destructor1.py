''''''
'''
 Destructor
 ----------
 - Destructor is a special method which destroys objects and releases 
  resourses tied to the objects.
  
- Destructor is called automatically on certain conditions.

- Destructor method is for ex: "__del__()"
        x = 100
        y = 200 
- Let 2 variables x & y we have to load the assigned values to the database 
  through database connection.
- So a DBObject will be created when the DBConnection is established.
 For file handling the obj. are also created inside the handlers.
 - Cache variables are also created in the memory.
 - Suppose we delete the variables x & y by using "del" keyword. Then,
 the memories occupied by these 2 variables are released (by garbage collection)
  but the memories occupied by the tied object are not released.
- In this type of situation the "Destructor" can be called to release 
  the memory.
- Conditions when destructor is called:
        - Reference counting reaches to zero
        - When variable goes out of scope.  
    
        

'''
class Employee:
    def  __init__(self,n,s):
        self.name = n
        self.salary = s
    def display(self):
        print(f"Name is {self.name}\n Salary is {self.salary}")

    # defining destructor
    def __del__(self):
        print('Destructor is called..')

e1 = Employee('RAM',45000)
# del e1

e1.display()
del e1  # destructor is executed automatically
print('Obj is deleted')
