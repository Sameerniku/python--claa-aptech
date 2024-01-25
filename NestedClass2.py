
class Student:
    def __init__(self, name, roll, dd=None, mm=None, yy=None):
        self.name = name
        self.roll = roll
        self.dob = self.DOB(dd,mm,yy)
    def display(self):
        print(f"Name :{self.name} and Roll no:{self.roll}")
        self.dob.display()

    class DOB:
        def __init__(self,dd,mm,yy):
            self.day = dd
            self.month = mm
            self.year = yy
        def display(self):
            print(f"Date of Birth : {self.day}/{self.month}/{self.year}")

s1 = Student('RAM',12,1,2,2010)
s1.display()