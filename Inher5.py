''''''
'''
Hierarchical Inheritance
------------------------
        A(Person)
  ------|-------      
  |             |
  B             C
  (Emp)       (Student)
  - When multiple child classes derived from a single base class is
    called Hierarchical Inheritance.
  - Here, 'B' & 'C' are 2 different classes inheriting a common class 'A'
  
'''
class Person:
    def __init__(self,n,a):
        self.name = n
        self.age = a

    def display(self):
        print('Name : ',self.name,'\n', 'Age:',self.age)

class Employee(Person):
    def __init__(self,n,a,sal):
        # self.name = n
        # self.age= a
        self.salary=sal
        super().__init__(n,a)

    def display1(self):
        print('Salary:',self.salary)

class Student(Person):
    def __init__(self,snm,sag,m):
        # print('Name :',snm,'Age:',sag,' Mark :',m)
        super().__init__(snm,sag)
        self.mark = m

    def display2(self):
        print('Mark :',self.mark)


s1 = Student('Shyam',12,90)
e1 = Employee('Ram',35,55000)
e1.display()
e1.display1()
s1.display()
s1.display2()

