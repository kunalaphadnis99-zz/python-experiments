# set1 = {5, 6, 7, 8, 1, 2, 3, 4, 9, 0}
# for item in set1:
#    print(f'Item is {item}')

# for item in 'Zero to Mastery':
#    print(f'Item is {item}')

user = {
    'name': 'Kunal',
    'age': 30,
    'is_employed': True
}
# for item in user:
#    print(item)

print('Keys:')
for item in user.keys():
    print(item)
print('----------------------')

print('Values:')
for item in user.values():
    print(item)
print('----------------------')

print('Items/Key-Value Pairs:')
for item in user.items():
    print(item)
print('----------------------')

print('Items/Key-Value Pairs 2:')
for item in user.items():
    print(f'{item[0]}: {item[1]}')
print('----------------------')

print('Items/Key-Value Pairs 3:')
for (key, value) in user.items():
    print(f'{key}: {value}')
print('----------------------')

print('Items/Key-Value Pairs 4:')
for key, value in user.items():
    print(f'{key}: {value}')
print('----------------------')

print('Items/Key-Value Pairs 5:')
for item in user.items():
    (key, value) = item
    print(f'{key}: {value}')
print('----------------------')
