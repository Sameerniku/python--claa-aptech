''''''
'''
Nested Class
------------
- The class within another class is known as nested class.

ex:
  class University:
            ----
        class College:
            -----
- It is required when one class obj. can not exist without another class obj.
- In this case, if there is no obj. for the outer class then,
  the inner class obj. also cannot be created.

'''

class Outer:
    def __init__(self):
        print('Outer class Constructor')
    def display(self):
        print('display() method of outer class')

    class Inner():
        def __init__(self):
            print('Inner class Constructor')
        def show(self):
            print('show() method of Inner class')

out1 = Outer()
out1.display()
inn1 = Outer.Inner()
inn1.show()
# inn1.display()
