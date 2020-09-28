# alike using statement in C# - with open('') as name
from decorators.decorators2 import performance_tracker


@performance_tracker
def write_lines_to_file(file_name, lines, mode):
    try:
        with open(file_name, mode=mode) as text_file:
            if not text_file:
                print('File does not exist.')
                return

            for (i, line) in enumerate(lines):
                text_file.write(f'Line {i + 1}: {line}\n')
            print('Written all lines to file')
    except Exception as e:
        print(f'Unable to write to file. Error: {e}')
    finally:
        pass


lines = ['This is a sample file',
         'This is a sample file',
         'This is a sample file',
         'This is a sample file']
write_lines_to_file('../static_resources/text_file.txt', lines, mode='w')
