''''''
'''
Abstraction
-----------
- Abstraction is a process by which data and functions are defined in such
   a way that only essential details can be seen and unnecessary 
   implementations are hidden.
- Means hiding complex implementation details and showing only signature 
  to the user.
- There is no built-in method/class available for abstraction like in
   java and c++ etc.
- By using "abc" module of Python we can achieve abstraction        
        abc module belongs to ABC class of Python.
- First inherit the class from ABC class,
  create abstract method in the abstract class.
- We cannot create an object of Abstract class.
    syntax:
        from abc import ABC, abstractmethod
        class Emp(ABC):
           -- abstract methods--
           -- concret methods --  

'''
from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def milage(self):
        pass
    def color(self):  # concrete method
        print('White')

class Maruti(Car):
    def milage(self):
        print('milage = 18 kmpl')

class Tata(Car):
    def milage(self):
        print('milage = 15 kmpl')

class Hundai(Car):
    def milage(self):
        print('milage = 21 kmpl')

# c1 = Car() # Error, we cannot create obj. of abstract class
m1 = Maruti()
t1 = Tata()
h1 = Hundai()

m1.color()
m1.milage()
t1.color()
t1.milage()
h1.color()
h1.milage()
'''
Use of Abstraction
------------------
- When we have a large code and functionalities,
- The abstract class is like an API for other subclasses
- It is used when a third party application requesting to access 
  some data.
- Different implementations for different objects of the same component.
Note:  
    Used for creating interfaces. 
     Abstract class having only abstract methods,
                                    no concrete methods.
'''