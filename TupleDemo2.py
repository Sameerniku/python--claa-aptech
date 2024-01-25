''''''
'''
Tuple Operations
----------------
 Addition of Tuples:
- Tuples can be added by using the concatenation operator (+) to
   join 2 or more tuples.

Replicating Tuples # Repeating the tuple elements
- It can be performed by using " * " with specifying no.of times.
  ex:  print(t1 * 2)
  
 Updation of a Tuple:
 --------------------
 - As tuples are immutable, so can't be editable/updatable.
 
 Deleting elements of a Tuple
 ----------------------------
 - Removing individual tuple elements is not possible.
 - We can delete the entire tuple explicitly by using
   " del " statement.  
    
'''

t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1 + t2
print('Tuple t3 after joining t1 & t2 :',t3)
print('Repeating t1 twice:')
print(t1 * 2)

print('Repeating t2 thrice:')
print(t2 * 3)

del(t1)
print('After deletion of t1,  t1 is',t1) # error, as deleted
