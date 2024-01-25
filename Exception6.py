class FiveDivisionError(Exception):
    "This Exception is called when we try to divide any num by 5  "
    pass
try:
    n1 = int(input('Enter 1st no:'))
    n2 = int(input('Enter 2nd no:'))
    if n2 == 5:
        raise FiveDivisionError('Cannot divide by 5')
    div = n1/n2
    print('Division: ',div)
except(FiveDivisionError,ZeroDivisionError,Exception)as var:
    print(var)
print('End of program..')