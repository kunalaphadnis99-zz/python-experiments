for (i, item) in enumerate(range(0, 100)):
    print(f'Item {i}: {item}')

for (i, item) in enumerate('My name is Ghantabhai Ghanteshwarprasad Tripathipavteshwar'):
    print(f'Item {i}: {item}')

for (i, item) in enumerate(list(range(100))):
    if item == 50:
        print(f'Index of 50 is {i}')
        break
