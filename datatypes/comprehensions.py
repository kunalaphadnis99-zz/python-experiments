# works with list, sets and dictionaries


print([char for char in 'kunalaphadnis'])
print([char.capitalize() for char in 'kunalaphadnis'])
print([char.upper() for char in 'kunalaphadnis'])
print([item for item in range(1, 101)])
print([item * 2 for item in range(1, 101)])
print([item * 2 for item in range(1, 101) if item % 2 == 0])
print({item * 2 for item in range(1, 101) if item % 2 == 0})
print({key: value for key, value in {'key1': 1, 'key2': 2, 'key3': 3} if value % 2 == 0})
