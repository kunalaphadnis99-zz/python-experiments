# generators are -> range which yield in memory like Enumerable in C# keep on yielding next


def generator_function(count):
    for i in range(count):
        yield i


for i in generator_function(100):
    print(i, end=' ')

print('')
generator = generator_function(100)
print(generator)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
