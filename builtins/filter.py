def is_even(item):
    return item % 2 == 0


print(list(filter(is_even, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])))
print(list(filter(is_even, [1, 2, 3, 4, 5, 6, 7, 8, 9, '0'])))  # not allowed
