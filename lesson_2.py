"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных
данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
a. Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие
и считывание данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения
параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра
поместить в соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список для хранения данных отчета — например,
main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС»,
«Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить
в файл main_data (также для каждого файла);

b. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение
данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
c. Проверить работу программы через вызов функции write_to_csv().

"""
# import csv
# from platform import system
# import re
# import chardet
#
# OSNAME = system().lower()
#
# FILE1 = 'info_1.txt'
# FILE2 = 'info_2.txt'
# FILE3 = 'info_3.txt'
#
# MASSIVE_FILES = [FILE1, FILE2, FILE3]
#
# MASSIVE_SEARCH_TEXT = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
#
# os_prod_list = []
# os_name_list = []
# os_code_list = []
# os_type_list = []
#
# main_data = []
#
#
# def type_file(file_open):
#     with open(file_open, 'rb') as f:
#         file_contest = f.read()
#         result = chardet.detect(file_contest)
#         return result['encoding']
#
#
# def get_data(massive_files, massive_search_text):
#     for i in range(len(massive_files)):
#         main_data.append([])
#         with open(massive_files[i], 'r', encoding=type_file(massive_files[i])) as f:
#             text_in_file = f.read()
#
#             # Search data in text
#             for el_search in massive_search_text:
#                 reg_exp = f'{el_search}.*'
#                 result = re.findall(reg_exp, text_in_file)
#                 if result:
#                     reg_sub = f'{el_search}:\s+'
#                     text_line = re.sub(reg_sub, '', result[0])
#                     # record to massive by element
#                     if el_search == massive_search_text[0]:
#                         os_prod_list.append(text_line)
#                         main_data[i].append(text_line)
#                     elif el_search == massive_search_text[1]:
#                         os_name_list.append(text_line)
#                         main_data[i].append(text_line)
#                     elif el_search == massive_search_text[2]:
#                         os_code_list.append(text_line)
#                         main_data[i].append(text_line)
#                     elif el_search == massive_search_text[3]:
#                         os_type_list.append(text_line)
#                         main_data[i].append(text_line)
#
#     main_data.insert(0, massive_search_text)
#     return main_data
#
# def write_to_csv(file_csv):
#
#     data = get_data(MASSIVE_FILES, MASSIVE_SEARCH_TEXT)
#     with open(file_csv, 'w') as f_out:
#         f_out_writer = csv.writer(f_out, quoting=csv.QUOTE_NONNUMERIC)
#         for row in data:
#             f_out_writer.writerow(row)
#     with open(file_csv) as f_read:
#         print(f_read)
#     with open(file_csv) as f_n:
#         f_n_reader = csv.reader(f_n)
#         f_n_headers = next(f_n_reader)
#         print('Headers: ', f_n_headers)
#         for row in f_n_reader:
#             print(row)
# write_to_csv('output_file.csv')
import yaml

"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. 
Написать скрипт, автоматизирующий его заполнение данными. Для этого:

a. Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity), 
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря 
в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;

b. Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""
#
# import json
#
#
# def write_order_json(item, quantity, price, buyer, date, file_to_write):
#
#     dict_to_json = {
#         'item': item,
#         'quantity': quantity,
#         'price': price,
#         'buyer': buyer,
#         'date': date
#     }
#     list_to_json = [
#         item,
#         quantity,
#         price,
#         buyer,
#         date
#     ]
#     with open(file_to_write, 'r+', encoding='utf-8') as f_write:
#         f_content_json = f_write.read()
#
#         #first key in file type string
#         f_content = json.loads(f_content_json)
#         key_in_file = list(f_content.keys())[0]
#         f_content[key_in_file] = list_to_json
#
#         # rewrite data to file
#         f_write.seek(0)
#         json.dump(f_content, f_write, sort_keys=True, indent=4)
#
#     with open(file_to_write, encoding='utf-8') as f_read:
#         f_read_content = f_read.read()
#         objs = json.loads(f_read_content)
#
#         print(objs)
#
#         # for section, commands in objs.items():
#         #     print(section)
#         #     print(commands)
# write_order_json('брюки', '3', '3500', 'Мажит', '25.01.2021', 'orders.json')


"""
3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата.
 Для этого:
a. Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, 
второму — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом,
 отсутствующим в кодировке ASCII (например, €);

b. Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. 
При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а также установить возможность 
работы с юникодом: allow_unicode = True;

c. Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""


DICT_TO_WRITE = {
    'one_key': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'two_key': 45,
    'three_key': {'1': '&', '2': 'Ф', '3': 'Ж'}
}

with open('file.yaml', 'w', encoding='utf-8') as f_write:
    yaml.dump(DICT_TO_WRITE, f_write)

with open('file.yaml', 'r', encoding='utf-8') as f_read:
    f_content = yaml.load(f_read, Loader=yaml.SafeLoader)
print(f_content)



