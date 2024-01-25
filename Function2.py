
def PURI():
    print('Within PURI')

def CTC():
    print('Within CTC')
    PURI()

def BBSR():
    print('Within BBSR')
    CTC()

print('Within main function')
BBSR()
CTC()
PURI()
print('Return to main function again..')