import os

from PIL import Image

path = '../'
directory = 'static_resources'

if not os.path.exists(directory):
    os.makedirs(directory)

path = path + directory + '/'

for filename in os.listdir(path):
    # if filename[0] == '.':
    #     continue

    clean_name = os.path.splitext(filename)[0]

    try:
        img = Image.open(f'{path}{filename}')
        img.save(f'{directory}{clean_name}.png', 'png')
    except:
        pass
    finally:
        print('all done!')
