''''''
'''
    Hybrid Inheritance
    ------------------
- When more than one inheritance concepts are applied to a single
  program it is called Hybrid Inheritance.
                Object
             ______|_____
ex:         P1          P2
            |            |
            ______________
                   |
                 Child
          _________|_______
          |               |
          C1              C2      
                       
-  Here, the problem is that, which class should be inherited first
   and in which path should compiler search the methods and attributes.
   
- To solve this problem, MRO concept is introduced by Python.       
- MRO means Method Resolution Order.
- MRO represents how properties (methods + attributes) are searched
  in inheritance. It has certain rules which are as follows:
   Rule 1:
    - Python first searches in child class and then goes to parent class.
      (Priority is given to the child class)
   Rule 2:
    - MRO follows 'Depth First Left to Right' approach.
  ex:         
        mro(O): Object
        mro(A): A,O
        mro(B): B,O
        mro(C): C,O
        mro(X): X,A,B,C,O
        mro(Y): Y,B,C,O
        mro(P): P,X,Y,A,B,C,O
  - MRO can be applied in all types inheritance.
  Rule 3:
    - We can use mro() method for knowing mro of any class objects.
    ex:
        class A:
           pass 
        class B:
           pass 
        class C:
           pass 
        class X(A,B,C):
           pass    
        class Y(B,C):
           pass            
        class P(X,Y):
           pass    
           
      
                   
'''


class A:
    pass

class B:
    pass

class C:
    pass

class X(A, B, C):
    pass


class Y(B, C):
    pass


class P(X, Y):
    pass

print(P.mro())
print(X.mro())
print(A.mro())