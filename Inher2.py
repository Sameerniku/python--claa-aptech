''''''
'''
 Use of constructors in Inheritance
 ----------------------------------
- Bydefault constructor of parent class is available to child classes.

- But when derived class has its own constructor, at that time 
  the derived class constructor will be called because it has the
   higher proirity than the parent class constructor.
 
'''
class BaseClass1:
    def __init__(self):
        print('Base class constructor')
        self.baseClassProperty = 'Var of Base Class'


class DerivedClass1(BaseClass1):
    def __init__(self):
        print('Derive class constructor')
        self.derivedClassProperty = 'Var of derived Class'
    # pass


d1 = DerivedClass1()
# print(d1.__init__())
print('Accessing derived class variable ',d1.__dict__)

'''
- Base class constructor is only accessed if child class constructor
  is not available, as child class constructor has the higher priority.

- This is called "Construcrot Overloading" 

'''
