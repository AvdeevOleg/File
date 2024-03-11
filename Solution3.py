def files_reader(file_list: list, output_file_name: str):
    files_dict_len = {}

    for file_name in file_list:
        with open(file_name, 'r', encoding='cp1251') as f:  # Изменено на cp1251
            for count, l in enumerate(f, 1):
                ...
            files_dict_len[count] = file_name
    sorted_len = dict(sorted(files_dict_len.items()))

    with open(output_file_name, 'w', encoding='utf-8') as n_f:
        for i in sorted_len.keys():
            with open(sorted_len.get(i), encoding='cp1251') as f:  # Изменено на cp1251
                n_f.write(str(sorted_len.get(i)) + '\n')
                n_f.write(str(i) + '\n')
                n_f.write(f.read().strip() + '\n')
    return ''

print(files_reader(['1.txt', '2.txt', '3.txt'], 'result_solution3.txt'))

