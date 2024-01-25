''''''
'''
 Polymorphism
 ------------
 - Polymorphism is a Greek word which means many forms.
 - In Python, polymorphism is an ability of a Python object 
   to take many forms.
 - If a variable / object/method performs different behaviour according to
   the situation, then it is called as "Polymorphism".
Ex:  
  The " + " operator behaves differently in different situations like in 
  numbers it adds them, where as in Strings it joins them.

- In case of built-in functions also polymorphism works differently
  in different situations. 
        
 



'''
a=10
b=5
c = a+b
print('Sum = ',c) # Here '+' is used to add to numbers

s1 = "Hi"
s2 = " Hello"
s3 = s1+s2
print('s1 + s2 is ',s3) # Here '+' is used to join two Strings

str1 = "Good Evening"
print("Length of str1 :",len(str1))
# Here len() counts the no.of characters in a string.

L1 = ['a','b','BBSR is a smart city']
print("Length of L1 :",len(L1))
 # Here len() counts the no.of items in a List.



