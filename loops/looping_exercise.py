picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]


def print_image(picture_array):
    for pixelsArray in picture_array:
        for pixel in pixelsArray:
            if pixel:
                print('*', end='')
            else:
                print(' ', end='')
        print(' ')


print_image(picture)
print_image(picture)
print_image(picture)
print(print_image)
print(type(print_image))
