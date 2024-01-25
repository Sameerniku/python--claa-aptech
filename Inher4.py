''''''
'''
Multi-level Inheritance
--------------------
- A parent class having a child class which is further 
  inherited to a new class is called multi-level inheritance.
 A
 |
 B
 |
 C
'''
class Employee:
    name = ''
    def __init__(self):
        print('Emp class cons')
    def setName(self):
        n = input('Enter your name:')
        Employee.name = n

    def getName(self):
        return Employee.name


class Salary(Employee):
    basic = 0.0

    def __init__(self):
        print('Salary class cons')

    def setSal(self):
        bs = float(input('Enter your Salary:'))
        Salary.basic = bs

    def getSal(self):
        return Salary.basic


class Bonus(Salary):
    bonus = 0.0
    def __init__(self):
        print('Bonus class cons')

    def getBonus(self):
        bonus = Salary.basic * 0.25
        return bonus

b1 = Bonus()
b1.setName()
b1.setSal()

print('Name',b1.getName())
print('Salary :',b1.getSal())
print('Bonus :',b1.getBonus())


