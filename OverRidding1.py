''''''
'''
 Over ridding
 -------------
- Over riding is a concept to redefine the built- in functions as
  per the user's requirments.
- ex:
    class Car:
         pass
    c1 = Car()
    print(c1)        
- c1 is the object present at particular location in memory.
- When print(c1) line is executed Python calls "__str__"method automatically.
 In this way many methods are called automatically in Python.
- It first checks whether "__str__" method is present in the above class "Car" 
  or not. If not available it checks in the library.
- It is the basic step defined when we print anything on o/p screen.
- But if we want to print our own message then, we can over ride it.
    


'''
class Car:
    def __str__(self):
        return "This is my personal msg."

c1 = Car()
print(c1)
