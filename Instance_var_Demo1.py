''''''
'''
Instance variables and Instance Methods
---------------------------------------
- In oops, we generally have 2 variables,
     i. instance variables
    ii. class variables
instance variables:
-------------------
- 



'''
class Student:
    def __init__(self,n,m):
        self.name  = n
        self.marks = m

s1 = Student('Ram',87)
s2 = Student('Shyam',88)
s3 = Student('Gopal',89)


print('Name and marks of Student 1 : ',s1.name,s1.marks)
print('Name and marks of Student 2 : ',s2.name,s2.marks)
print('Name and marks of Student 3 : ',s3.name,s3.marks)
'''
# We can also add a new instance var with the help of obj.
# We can also modify instance var with the help of obj.
'''
s1.age=21
s1.name = 'Ram Kumar'
print('Name, marks and Age of Student 1 : ',s1.name,s1.marks, s1.age)
'''
- We can delete an instance var with the help of the obj. using "del"
'''
del s1.marks
print('Name and Age of Student 1 : ',s1.name, s1.age)




