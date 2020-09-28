list_range = range(0, 100, 2)  # start, stop, stepover, -1 stepover for reversing
print(type(list_range))

my_list = list(list_range)
print(my_list)

for item in range(0, 100):
    print(item)

for _ in range(0, 100):
    print(_)

for item in range(100, 0, -1):
    print(item)

set = list(range(0, 100))
new_set = set[::-1]
print(new_set)
