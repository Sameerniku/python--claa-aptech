class Student:
    def __init__(self,n,m):
        self.name  = n
        self.marks = m
    def display(self):  # instance method
        print(self.name,self.marks)

    def change_data(self): # another instance method
        self.name = input('Enter your new name:')
        self.marks = int(input('Enter your new mark:'))
'''
- with the help of the instance methods we can change the data
  of the instance variables.
'''
s1 = Student('Ram',87)
s2 = Student('Shyam',88)
s3 = Student('Gopal',89)
s2.change_data()
s2.display()



'''
print('Name and marks of Student 1 : ',s1.name,s1.marks)
print('Name and marks of Student 2 : ',s2.name,s2.marks)
print('Name and marks of Student 3 : ',s3.name,s3.marks)
'''


