''''''
'''
read():
-------
- It is used to read a string from an opened file.
- It is important to note that Python Strings can have 
  binary data apart from text data.


'''
f1 = open('D:\Demo1.txt','r')
readdata = f1.read()
f1.close()
print(readdata)
f1 = open('D:\Demo1.txt','r')
readdata = f1.read(10)
f1.close()
print(readdata)




