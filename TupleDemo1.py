''''''
'''
Tuple
-----
- A tuple is a sequence of immutable python objects.

- Tuples are sequences just like list, but the difference is 
  tuples cannot be changed like List.

- Tuples uses parenthesis() where as Lists uses [].
 ex:  T1()
 Accessing values in Tuples
---------------------------- 
- To access the elements of a Tuple, use the square brakets[]
 for slicing along with the index to obtain the values.
 
 syntax:  
       tuple[index]  # for individual element
       
       tuple[ start : stop : step ] # slicing for group of elements
          , bydefault step is 1.


'''

t1 = ('a','b','c',1,2,3,4,5.12345,"Happy Durga Puja!!!")
print('Tuple t1 = ',t1)
# We can insert a List within a Tuple

t2 = (11,22,33,[101,202,303])
print('Tuple t2 = ',t2)
print()
print('Tuple in forward indexing:')
print('t1[0] = ',t1[0])
print('t1[1] = ',t1[1])
print('t1[2] = ',t1[2])
print('t1[3] = ',t1[3])
print('List in Revers indexing:')
print('t1[-1] = ',t1[-1])
print('t1[-2] = ',t1[-2])
print('t1[-3] = ',t1[-3])
print('t1[-4] = ',t1[-4])

print('t2 = ',t2[0:3:1])  # using slicer

