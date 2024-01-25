''''''
'''
  super():
  -------
- By using super() method we can call the base class constructor
  with the help of child class object. 

- This function returns a temporary object which contains
  reference to the parent class.
  
- It makes inheritance manageable  & extensible. 

'''
class Computer(object):
    def __init__(self):
        self.ram = '16GB'
        self.storage = '1TB'
        print('Base class cons. is called')

class Mobile(Computer):
    def __init__(self):
        super().__init__()
        self.camera='50MPX'
        print('within Mobile')

m1 = Mobile()

print(m1.__dict__)


