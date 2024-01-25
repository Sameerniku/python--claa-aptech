class Employee:

    def __init__(self,n,a):
        self.name = n
        self.age  = a


    def display(self):
        print('Name : ',self.name)
        print('Age  : ', self.age)

e1 = Employee('RAM',21)
e2 = Employee('SHYAM',22)
# e3 = Employee()

e1.display()
e2.display()
# e3.display()

