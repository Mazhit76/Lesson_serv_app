# """
# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип
# и содержание соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые
# представление в формат Unicode и также проверить тип и содержимое переменных.
# """
#
# value_str1 = 'разработка'
# value_str2 = 'сокет'
# value_str3 = 'декоратор'
#
# massive_value = [value_str1, value_str2, value_str3]
#
# for i in range(len(massive_value)):
#     print(f'Значение переменной: {massive_value[i]}, тип:  {type(massive_value[i])}')
#
#
# value_str1_unicode = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
# value_str2_unicode = '\u0441\u043e\u043a\u0435\u0442'
# value_str3_unicode = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
#
# massive_value_unicode = [value_str1_unicode, value_str2_unicode, value_str3_unicode]
#
# for i in range(len(massive_value_unicode)):
#     print(f'Значение переменной: {massive_value_unicode[i]}, тип:  {type(massive_value_unicode[i])}')
#
#     print(f' Равенство значениий строк в формате  str и unicode: {massive_value_unicode[i]==massive_value[i]}')



# """
# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность
# кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
# """
#
# value_str1 = b'class'
# value_str2 = b'function'
# value_str3 = b'method'
#
# massive_value = [value_str1, value_str2, value_str3]
#
# for i in range(len(massive_value)):
#     print(f'Значение переменной: {massive_value[i]}, тип:  {type(massive_value[i])} длина: {len(massive_value[i])}')



"""
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
"""
#
# value_str1 = b'attribute'
# # value_str2 = b'класс'
# # value_str3 = b'функция'
# value_str4 = b'type'

#  Строки содержащие кириллицу невозможно записать в байтовом представлении из-за отсутствия их в кодировке  ASCII,
#  без использования методов encode(с добавлением знака 'b' перед строкой.)


"""
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового
 представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).
"""

# value_str1 = 'разработка'
# value_str2 = 'администрирование'

# value_str3 = 'protocol'
# value_str4 = 'standard'
#
# massive_value = [value_str1, value_str2, value_str3, value_str4]
#
# for i in range(len(massive_value)):
#     value_byte = str.encode(massive_value[i], encoding='utf-8')
#     value_str = bytes.decode(value_byte, encoding='utf-8')
#     print(f' В байтовом представлении: {value_byte},  в строковом выражении:  {value_str}')


"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и 
преобразовать результаты из байтовового в строковый тип на кириллице.
"""

# import subprocess
# import chardet
# massive_web_host = ['yandex.ru', 'google.com']
# for web_host in massive_web_host:
#     subpoc_ping = subprocess.Popen(["ping", "-c", "4", web_host], stdout=subprocess.PIPE)
#     for line in subpoc_ping.stdout:
#         result = chardet.detect(line)
#         line = line.decode(result['encoding'])
#         line = line.encode('utf-8')
#         print(line.decode('utf-8'))


"""
6.  Создать текстовый файл test_file.txt, заполнить его тремя строками: 
«сетевое программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию. 
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""

import chardet

# with open('test_file_lesson1.txt', 'w+') as f:
#     f.write("сетевое программирование\n")
#     f.write("сокет\n")
#     f.write("декоратор\n")
#     f.close()

# with open('test_file_lesson1.txt', 'r') as f:
#     file_contest = f.read()
#     print(type(file_contest))

#     result = chardet.detect(str.encode(file_contest))
#     print(result)

with open('test_file_lesson1.txt', 'r', encoding='utf-8') as f:
    file_contest_unicode = f.read()

    file_contest_unicode_bytes = str.encode(file_contest_unicode, encoding='utf-16')
    print(file_contest_unicode_bytes)

    result = chardet.detect(file_contest_unicode_bytes)
    print(result)

    print(bytes.decode(file_contest_unicode_bytes, encoding=result['encoding']))





