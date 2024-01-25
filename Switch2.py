# By using "match case" will not run as its version is 3.9
'''
choice = eval(input('Enter your choice:'))
match choice:
    case 'ab':
        print('with in case ab')
    case [1,2,3]:
        print('within list[1,2,3]')
    case 'cd':
        print('within case cd ')
'''