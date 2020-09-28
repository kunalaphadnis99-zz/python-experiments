def add_numbers(num1, num2):
    return num1 + num2


def divide_numbers(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError as error:
        return error


def multiple_numbers(num1, num2):
    return num1 * num2


def subtract_numbers(num1, num2):
    return num1 - num2
