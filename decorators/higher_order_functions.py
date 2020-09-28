def hello():
    print('Hello')


greet = hello
print(f'Hello ref before del {hello}')
print(f'Greet ref before del {greet}')
del hello
print('Deleted hello name ref')
# print(hello) - throws error as hello name ref is deleted
print(greet)
print(f'Greet ref after del {greet}')

# del hello # deletes the name reference
greet()

# you can even pass functions as arguments and call them from the called functions
