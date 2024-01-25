''''''
'''
# Before Encapsulation
class Finance:
    def __init__(self):
        self.revenue = 100000
        self.no_of_sales = 115

f1 = Finance()
print(f1.__dict__)

class HR:
    def __init__(self):
        self.no_of_emp = 45
        # print(f1.revenue)
        f1.revenue = 1
        print(f1.revenue)

h1 = HR()
print(f1.__dict__)
'''
'''
- Here, in this case the property of class "Finance" is getting modified
  within class "HR" which makes the data insecure in class "Finance".
  
- To avoid this, we need "Encapsulation" where data protection is applied.
'''
# By using Encapsulation
# class Employee:
#     def __init__(self,n,s):
#         self.name = n
#         self.salary = s
#
#     def display(self):
#         print("Name : ",self.name)
#         print('Salary : ',self.salary)
#
# obj = Employee('Ram',45000)
# print(obj.name)
# print(obj.salary)

'''
- Encapsulation can be achieved by declaring the data members and methods 
  of the class as "private"
  
- There are 3 access specifiers available in python,
        - public
        - private
        - protected
- public members:
        - Accessable from any where by using object reference.
- private member:
        - Accessable within the class only, through the methods.
        - Can't access from outside the class by using object reference.
- protected member:              
        - Accessable within class and its sub classes
        - Used in case of Inheritance(rarely)
        
- To make a data as private add two underscores(__) before the 
  variable name.
- To make data as protected , just ass a single underscore(_).
          
'''

class Finance:
    def __init__(self):
        self.__revenue = 100000   # private data
        self._noofsales = 115  # protected data


f1 = Finance()
print(f1.__dict__)
# f1.revenue = 105  # no impact on original variable
# print(f1.revenue) # Error, as private
print(f1._noofsales) # No error as protected
class HR:
    def __init__(self):
        self.no_of_emp = 45
        # print(f1.revenue)
        # f1.revenue = 1
        # print(f1.revenue)

h1 = HR()
print(h1.__dict__)
