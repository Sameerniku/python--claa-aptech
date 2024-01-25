# Factorial of a no.
# def fact(x):
#     f=1
#     while x > 0:
#         f = f * x
#         x-=1
#     return f
# n = int(input('Enter a no:'))
# print('Factorial of ',n,' is ',fact(n))

'''
Swapping of 2 nos.
'''
# def swap(a,b):
#     print('Before swapping a : ',a,' b : ',b)
#     temp = a
#     a = b
#     b = temp
#     print('After swapping a : ', a, ' b : ', b)
#
# x = int(input('Enter 1st no:'))
# y = int(input('Enter 2nd no:'))
# swap(x,y)
#
'''
Armstrong number ex: 153 
'''
# n = int(input('Enter a no:'))
# armstrong(n)
def armstrong(x):
    x1 = x
    sum = 0
    while(x>0):
        rem = x % 10
        sum = sum + (rem ** 3)
        x = x //10
    if(x1 == sum):
        print(x1,' is an Armstrong no.')
    else:
        print(x1, ' is not an Armstrong no.')

n = int(input('Enter a no:'))
armstrong(n)
