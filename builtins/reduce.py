from functools import reduce

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, list1, 0))
