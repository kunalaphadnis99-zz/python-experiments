def multiple_by2(item):
    return item * 2


print(list(map(multiple_by2, [1, 2, 3, 4, 5, 6, 7, 8, 9, '0'])))
print(list(map(multiple_by2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])))
print(list(map(multiple_by2, [])))
print(list(map(multiple_by2, '')))
print(list(map(multiple_by2, 'TRUE')))  # ['TT', 'RR', 'UU', 'EE']
print(list(map(multiple_by2, True)))  # not allowed because bool is not iterable
