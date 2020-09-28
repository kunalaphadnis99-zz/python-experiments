# set is an unordered collection of unique values
my_set = {1, 2, 3, 8, 9, 0, 0, 4, 5, 6, 7}

print(type(my_set))
print(my_set)

my_set.add(2)
my_set.add(100)
print(my_set)

array = [1, 2, 3, 4, 5, 5, 6, 5, 5]
new_array_set = set(array)
array.clear()
print(array)
print(new_array_set)
print(f'Value existence {1 in new_array_set}')

set1 = {1, 2, 3}
set2 = {1, 4, 5, 6, 7, 0}
print(f'Difference: {set1.difference(set2)}')
set2.discard(0)
print(f'Post-discard 0 from set: {set2}')
print(f'Difference: {set1.difference(set2)}')
print(f'Intersection: {set1.intersection(set2)}')
print(f'Union: {set1.union(set2)}')
