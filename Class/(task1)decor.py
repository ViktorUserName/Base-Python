
def dec(func):
    def wrap(*arg, **kwarg):

        for i in range(len(*arg)+2):
            if i != len(*arg)+1:
                print('*', end='')
            else:
                print('*', end='\n')


        print('*', end='')
        func(*arg, **kwarg) 
        print('*', end='')

        for i in range(len(*arg)+2):
            if i == 0:
                print('', end='\n')
                print('*', end='')
            else:
                print('*', end='')

    return wrap

@dec
def sayHi(text):
    print(text, sep='',end='')

sayHi("Python")