class Finance:
    def __init__(self):
        self.__revenue = 100000  # private data
        self.__noofsales = 115  # protected data
    def display(self):
        print(f"revenue:{self.__revenue} and no.of sales : {self.__noofsales}")
        self.__revenue = 200000
        self.__noofsales = 125
        print(f"revenue:{self.__revenue} and no.of sales : {self.__noofsales}")


f1 = Finance()
f1.display()
# print(f1.revenue) # Error, as private variable cannot be accessed from
                    # outside class even with the help of the object.
# f1.display()
'''
- By using methods we can access the private members only
  (can't access directly)
- We can also modify these variables within the method
  (getter and setter methods)  
  
- So we can say Encapsulation concept is not directly implemented in Python,
  it is only used to avoid accidential modification of variables.
  (By using private( "__" ) access specifiers.  
'''



class HR:
    def __init__(self):
        self.no_of_emp = 45
        f1.__revenue = 1234



h1 = HR()
print(h1.__dict__)

