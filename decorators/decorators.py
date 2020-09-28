def my_decorator1(func):
    def wrapped_func():
        print('Before executing...')
        func()
        print('After executed...')

    return wrapped_func


def my_decorator2(func):
    def wrapped_func(func2):
        print('Before executing...')
        func(func2)
        print('After executed...')

    return wrapped_func


def my_decorator3(func):
    def wrapped_func(*args, **kwargs):
        print('Before executing...')
        func(*args, **kwargs)
        print('After executed...')

    return wrapped_func


@my_decorator1
def my_func():
    print('hello')


@my_decorator2
def my_func2(greeting):
    print(greeting)


my_func2('greeting')
# my_func()
# print('------------------------------------')
# my_decorator1(my_func)() # same as above
