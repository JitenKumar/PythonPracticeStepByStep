# decorator is used to add extra functionalities to the existing function

def i_am_decorator(old_func):

    def wrapper():

       #print('Extra code can be put here before the old_func()')

        print('Do you want to be more powerful???')
        print('')

        old_func()

        print('training you inner strength you should be able to feel the force inside you')
        print('Now You are the most decorated Master Jedi bro ')
        print('MAY THE FORCE BE WITH YOU ')

    return wrapper


@i_am_decorator
def i_need_a_decorator():
    print('Yes.... Please Decorate me and make me more powerful')


print(i_need_a_decorator())
