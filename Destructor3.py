''''''
'''
 Destructor in case of Exception Handling
 ----------------------------------------
 - When exception occures in constructor( __init__() ), as we know
   a constructor is called when the obj. is initialized. 
- But at the time of execution the constructor, if an exception arises then, 
  constructor is not called properly and destructor is called which
   clears all the resources, in this case another exception may arise.     

'''
class NAge(Exception):
    pass
class Age:
    def __init__(self,age):
        if age < 0:
            raise NAge('Age cannot be Negative')

    def __del__(self):
        print('Destructor is called')

a1 = Age(-10)

'''
- In the output the exception is arised(user defined exception),
  still the desturctor is called.
- So we have to be more focused while writing destructors.   



'''