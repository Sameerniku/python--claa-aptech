''''''
'''
Disadvantages of Destructor:
----------------------------
- It will not work properly in circular referencing.
- Circular referencing means, when two objects are referencing
  to each other.

'''
import time
class Teacher:
    def __init__(self,obj2):  #4
        self.obj2 = obj2

    def __del__(self):
        print('Teacher class Destructor is called.')
class Student:
    def __init__(self,num):  #2
        self.rollno = num
        self.obj1 = Teacher(self) #3

    def __del__(self):
        print('Student class Destructor is called.')

s1 = Student(10)#1
del s1
time.sleep(5)  #5
'''
- It will sleep for 5 sec and then both the destructors are called.

- But according to the code the program first "s1" object should be 
  created and then, at the time of "del s1" the destructor should be
  called which is not happening.
  So we can say the destructor concept is not working properly in case
  of circular referencing.
 '''