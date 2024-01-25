''''''
'''
 RECURSION
 ---------
 - When a function calls itself again and again it is called "Recursion".
 
 - It is an alternative of loop.
 
 - A loop might be executed infinite times in other prog. languages but 
   in Python it is restricted to 1000 times only.
 
 - Advantages:
        -   clean code
        -   Complex problems can be resolved.
 - Dis-advantages:
        - Difficult to debug.
        - Not memory efficient.        
 
'''
i=0
def demo():
    global i
    i = i + 1
    print('Hello :',i)
    demo()

demo()




