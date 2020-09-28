list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
list2 = [1, 2, 'A', 'B', 'C', 'D']
# list2 = [1, 2, 'A', True]

print(list1)
print(list1[:])
print(list1[0:2])
print(list1[2:5])
print(list1[:len(list1)])

list1[0] = 'Kunal'
print(list1)

# list slicing creates a new list
new_list1 = list1[0:3]
print(new_list1)

# To copy a list as it is without creating a new list and having only a reference
new_list2 = list2
print(f'New list reference: {new_list2}')

# To copy a list as it is with creating a new list
new_list3 = list2[:]
print(f'New list instance: {new_list3}')
new_list4 = list2.copy()
print(f'New list instance: {new_list4}')

matrix = [
    [1, 2, 3],
    [1.1, 1.2, 1.3],
    [2.1, 2.2, 2.3],
    [3.1, 3.2, 3.3]
]
print(matrix[2][2])
print(1 in matrix[0])

list_range = list(range(1, 100))
print(list_range)

item_list = ['Hi!', 'My', 'name', 'is', 'Kunal.']
joined_items = ' '.join(item_list)
print(joined_items)

# list unpacking
a, b, c = [1, 2, 3]
x, y, z = 1, 2, 3
l, m, n = {1, 2, 3}
q, r, s, *others, j = [1, 2, 3, 4, 5, 6]
print(m)
