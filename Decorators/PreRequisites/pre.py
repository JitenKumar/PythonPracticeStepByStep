# returning a function from a function
def main_fun(name='Jiten'):

    print('This is the main func')

    def first():
        print('First function inside the main_fun()')

    def second():
        print('Second function inside the main_fun()')

    print('Function is going to return now')
    if name == 'Jiten':
        return first
    else:
        return second


some_fun = main_fun('Jitender')
print(some_fun())


# PASSING FUNCTION AS AN ARGUMENTS TO A FUNCTION

def funct():
    return 'Hey this is me Jitender'


def func1(some_fun):
    print('This is the func1')
    return some_fun()


some_val = func1(funct)
print(some_val)


