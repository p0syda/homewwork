import os

def count_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return len(file.readlines())

def merge_files(file_list, output_file):
    file_list.sort(key = count_lines)

    with open(output_file, 'w', encoding='utf-8') as out_file:
        for file_name in file_list:
            lines_count = count_lines(file_name)
            out_file.write(f"{file_name}\n{lines_count}\n")
            with open(file_name, 'r', encoding='utf-8') as in_file:
                out_file.write(in_file.read())

file_list = ['1.txt', '2.txt']
output_file = 'result.txt'
merge_files(file_list, output_file)