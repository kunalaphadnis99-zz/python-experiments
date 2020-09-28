# simple function implementation


def print_something(name='No Name', emoji='No Emoji'):
    print(f'Hi {name}! {emoji}')


# positional arguments
print_something('Kunal', ':)')
print_something('Jui', ':)')

# keyword arguments
print_something(emoji=':)', name='keyword arguments')  # bad practice

print_something('Kunal')


def sum(num1, num2):
    return num1 + num2


(num1, num2) = 4, 5
addition_result = sum(num1, num2)
print(f'Addition result of {num1} and {num2} is {addition_result}')


# local internal functions
def sum1_external(num1, num2):
    def sum2_internal(num1, num2):
        return num1 + num2

    return sum2_internal(num1, num2)


addition_result_sum1_external = sum1_external(num1, num2)
print(f'Addition result of {num1} and {num2} is {addition_result_sum1_external}')

# methods vs functions
'some string value'.capitalize()  # method
sum(4, 5)  # user-defined function
range(0, 100)  # built-in function


def print_something(value):
    """
    Prints a given value to the console
    :param value: value string
    :return: None
    """
    print(value)


help(print_something)
print('')
print(print_something.__doc__)


def is_even_number(num):
    return num % 2 == 0
    # return True if num % 2 == 0 else False


print(is_even_number(50))
print(is_even_number(51))
print(is_even_number(52))
print(is_even_number(53))

print('Even/Odd from range')
list = range(0, 101)
for (i, item) in enumerate(list):
    print_message = 'even' if is_even_number(item) else 'odd'
    print(f'{item} is {print_message}')
