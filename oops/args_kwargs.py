# *args
def args_function1(*args):
    return sum(args)


print(args_function1(1, 2, 3, 4, 5, 6))


def args_function2(*args):
    for (i, item) in enumerate(args):
        print(f'Argument at {i} is {item}')


args_function2(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)


def args_kwargs_function1(*args, **kwargs):
    kwargs_sum = 0
    for item in kwargs.values():
        kwargs_sum += item
    return sum(args) + kwargs_sum


addition_result = args_kwargs_function1(1, 2, 3, 4, 5, 6, num1=10, num2=20, num3=30, num4=40)
print(addition_result)


# standard format for using parameters: params, *args, default params, **kwargs
def some_function(param1, param2, *args, default1='', default2=101, **kwargs):
    pass
