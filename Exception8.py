''''''
'''
 Exception in File handling
 --------------------------
- When we are dealing with files, the Exception may arise due to,
       - impropper path
       - File does not exist
         etc..

'''
try:
    f = open("D:\Demo1.txt",mode='r')
    print('File exists..')
except Exception as var:
    print(var)
else:
    f.close()
print('Rest of the code')




