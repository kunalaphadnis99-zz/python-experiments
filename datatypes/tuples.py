tuple = (1, 2, 3, 4, 5, 6)

print(1 in tuple)

new_tuple = tuple[:]
tuple = None

print(tuple)
print(new_tuple)

a, b, c = [1, 2, 3]
x, y, z = 1, 2, 3
l, m, n = {1, 2, 3}
print(m)

q, r, s, *others, j = [1, 2, 3, 4, 5, 6]
print(f'Others: {others}')
print(f'Last j: {j}')
