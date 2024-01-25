''''''
'''
File Handling in Python
-----------------------
opening a file:
---------------
- To open a file, we can use the built-in function "open()" 

- It returns an object of file which is used with other functions.

- After opening a file we can perform read/write/append operations on it.

Closing a file:
---------------
- The close() function is used to close an opened file.
- It flushes any unwritten information and closes the file object 
  after which no more writing can be done.
- It is a good practice to close the file immediately after complition of writing operation.


Attributes of file object:
---------------------------
file.closed : it returns "True" if file is closed and returns "False" otherwise.

file.mode : Returns the access mode of the file.

file.name  : Returns the name of a file.

write():
----------
- Used to write a string into the file.

- It does not add a new line character('\n') at the end of the string.
'''
file1 = open('D:\Demo1.txt',"w")
file1.write('Happy Kali Puja & Dhan Terash....')

file1.close()

print('File created successfully...')


















