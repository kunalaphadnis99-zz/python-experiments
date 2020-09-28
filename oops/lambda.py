# lambda param: action(param)
from functools import reduce


def lambda_resolver(item):
    return item * 2


print(list(map(lambda item: lambda_resolver(item), [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])))
print(list(map(lambda item: item * 2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])))
print(reduce(lambda acc, item: acc + item, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
