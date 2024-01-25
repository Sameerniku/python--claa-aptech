class Book:
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages
        # Without this method Compilation Error will arise
        # Here, we are redefining the __add__()
    def __add__(self, other):
        total = self.pages + other.pages
        return total

b1 = Book('Phy',300)
b2 = Book('Chem',200)

print('Total pages:', b1+b2)
'''
- Here an error msg will appear because when it trys to add b1 & b2 
  it could not find the type b1 & b2 as type<Book> is undefined.
- So we have to define the add operation with the identification
  of b1 & b2 first with in the __add__() method   

'''