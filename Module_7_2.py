def custom_write(file_name: str, strings: list):
    string_positions: dict = {}
    file = open(file_name, 'a', encoding='utf-8')
    for i in range(0, len(strings)):
        str_num = i + 1
        str_start = file.tell()
        file.write(strings[i])
        file.write('\n')
        string_positions[(str(str_num), str(str_start))] = strings[i]
    file.close()
    return string_positions


info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
