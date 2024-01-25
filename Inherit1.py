''''''
'''
 Inheritance
 -----------
 - It is the process of deriving the properties of base class 
   to the child class with out recreating it.
   
 - It's main advantage is code reusability.  

class Base/Parent/Super:
     #attributes & methods
     
class Derived/Child/Sub(Base/Parent/Super):
     #attributes & methods


'''
class Employee:
    bonus=2000
    def display(self):
        print('This is Employee(Base) class Method')
        x=10
        print(' x = ',x)
    def show(self):
        print('show() of Employee class')

class Manager(Employee):
    def show(self):
        print('This is Manager(Derived) class Method')
        print('bonus : ',Employee.bonus)


e1 = Employee()
m1 = Manager()

m1.display()
m1.show()

'''
- We can access the properties of the Parent class within child class
  but we cannot access the properties of child class in Parent class.
  
- class variables and instance variables can also be inherited.
  
  
  
'''








