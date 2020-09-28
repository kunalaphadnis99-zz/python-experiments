from decorators.decorators2 import performance_tracker


@performance_tracker
def open_files(file_names):
    for (i, item) in enumerate(file_names):
        try:
            text_file = open(item)
            # print(text_file.name)
            # print(text_file.read())

            if text_file:
                # print(text_file.read())
                print(
                    f'File #{i + 1} with name: {text_file.name}, enoding: {text_file.encoding}, mode: {text_file.mode}, size: {text_file.__sizeof__()} was opened successfully.')
                text_file.close()
            else:
                pass
        except Exception as e:
            print(f'File #{i + 1} with name {item} failed to open. Error: {e}')
            # print(f'Error in reading file. Error: {e}')


file_names = ['../static_resources/text_file.txt', '../static_resources/not_existent_file.txt']
open_files(file_names)
# if you want to read the same file again, then use .seek(0) before reading it again

# text_file = open('text_file.txt')
# for (i, line) in enumerate(text_file.readlines()):
#    print(f'Line {i + 1}: {line}')
