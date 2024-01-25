''''''
'''
  Class Variables and Class Methods
  ---------------------------------
- Class variables are declared for the entire class.

- There is only copy of the class variable available in the memory
  and distributed among all the objects.
  i.e. whenever  the variable is called with the help of the 
   object(s), only one space for the variable is assigned in the 
   memory. (many obj. sharing the same variable) 

- But they can't modify the variable, because, modification in class 
  variable impacts on all the objects.

'''

'''
 Change the class variable using class method.
 Class Method:
 -------------
 - It is a method which works on class variables.

 - It's first arg is class reference(cls)

 - We should use a decorator '@classmethod' to define it.

'''
class Student:
    city='BBSR'  # class variable
    def __init__(self,n,m):
        self.name = n
        self.mark = m

    @classmethod   # Decorator for class method
    def get_city_name(cls):
        print("Before modification City: ", cls.city)
        cls.city="CTC-123"
        return cls.city

Student.get_city_name()
print('After modification:',Student.city)
s1 = Student('Ram',89)
s2 = Student('Shyam',90)
s3 = Student('Gopal',92)

print('Name :',s1.name)
print('Mark :',s1.mark)
print('City :',s1.city)
# s1.city="xyz"
# print('City :',s1.city)

print('Name :',s2.name)
print('Mark :',s2.mark)
print('City :',s2.city)

print('Name :',s3.name)
print('Mark :',s3.mark)
print('City :',s3.city)
