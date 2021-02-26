# 1.	Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку
# определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV.
# Для этого:
# a.	Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными,
# их открытие и считывание данных. В этой функции из считанных данных необходимо с помощью регулярных
# выражений извлечь значения параметров «Изготовитель системы»,  «Название ОС», «Код продукта», «Тип системы».
# Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка — например,
# os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для хранения
# данных отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка:
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также оформить
# в виде списка и поместить в файл main_data (также для каждого файла);
# b.	Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать
# получение данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
# c.	Проверить работу программы через вызов функции write_to_csv().
import csv, re



def get_data(find_str, name_file):
    # Перебирает все файлы и заносит данные в список
    def in_data(file_name, mas_file=[]):
        for i in file_name:
            with open(i, encoding='cp1251') as f_n:
                mas_file.append(list(csv.reader(f_n)))
        #         В задании указано открывать как csv файл, хотя можно было открыть его как просто файл и читать и на
        #           один цикл было бы меньше
        return mas_file

    # На входе получает список файлов и поисковую строку , по ней находит все вхождения
    # в файлах и заносит в список на выходе список с найденными эл-ми
    def find_data(find_str='', mas_file=[]):
        massiv_out = []
        pattern = re.compile(find_str+':')
        for el_mas in mas_file:
            for value in el_mas:
                for line in value:
                    # if find_str in line:
                    if pattern.match(line):
                        # massiv_out.append(line[len(find_str)+2:].strip())
                        m = pattern.sub('', line).lstrip()
                        massiv_out.append(m)
        return massiv_out

    mas_file = in_data(name_file)


    os_prod_list = find_data(find_str[0], mas_file)
    os_name_list = find_data(find_str[1], mas_file)
    os_code_list = find_data(find_str[2], mas_file)
    os_type_list = find_data(find_str[3], mas_file)


    main_data = [find_str, os_prod_list, os_name_list, os_code_list, os_type_list]

    to_file = 'main_data.csv'
    with open(to_file,'w') as f_w:
        f_n_writer = csv.writer(f_w)
        f_n_writer.writerows(main_data)

find_str = ['Изготовитель системы',  'Название ОС', 'Код продукта', 'Тип системы']
name_file = ['info_1.txt', 'info_2.txt', 'info_3.txt']

get_data(find_str, name_file)



# 2.	Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
# Написать скрипт, автоматизирующий его заполнение данными. Для этого:
# a.	Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
# цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде
# словаря в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
# b.	Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.

import json

def write_order_to_json(item, quantity,price, buyer, date):
    dict_to_json = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    }
    with open('orders.json', encoding='utf-8') as f_n:
        data = json.load(f_n)

    data['orders'].append(dict_to_json)

    with open('orders.json', 'w') as f_w:
        json.dump(data, f_w, indent=4)

    with open('orders.json', encoding='utf-8') as f_n:
        line = json.load(f_n)
        print(line)

write_order_to_json('Колбаса', '5','250','Иваев Мажит','25.02.2021')

# 3.	Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в
# файле YAML-формата. Для этого:
# a.	Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список,
# второму — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом,
# отсутствующим в кодировке ASCII (например, €);
# b.	Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить
# стилизацию файла с помощью параметра default_flow_style, а также установить возможность работы с
# юникодом: allow_unicode = True;
# c.	Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.


data = {
    'one': ['one', 'two', 'три'],
    'two': 2,
    'three': {
        'four': '123€',
        'five': '\u0440'
    }
}

import yaml

with open('file.yaml', 'w') as f_w:
    yaml.dump(data, f_w, default_flow_style=False, allow_unicode=True)
with open('file.yaml') as f_r:
    f_content = yaml.load(f_r,  Loader=yaml.FullLoader)
print(f_content)

