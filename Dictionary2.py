''''''
'''
 Updating Dictionary Elements
 ----------------------------
 - We can update a dictionary by adding a new entry
   or, by modifying an existing entry(key:value pair). 
 Deleting elements:
 ------------------
 - 'del' statement is used to perform the delete operation,
    its done with the help of the key.
 ex:   del dict[3] 
- To remove all the elements we can use "clear()"


'''
d1={1:"BBSR", 2:"CTC", 3:"PURI"}
print('Dictionary before Modification: ',d1)

d1[4] = "Sambalpur"
d1[5] = "Koraput"
d1['State']= 'Odisha'
d1['State']= 'MP' # modified to MP
d1[1]='Bhubaneswar'
print('Dictionary after Modification: ',d1)
del d1[3],d1[4]
print('Dictionary after deletion of key = 3 & 4 : ')
print(d1)
print('Dictionary after using clear() : ')
d1.clear()
print(d1)  # empty dictionary
# print(d1[5]) # Error, as already empty dict.
