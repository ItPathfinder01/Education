# Task 1
# Reading files
with open("welcome.txt") as text_file:
  text_data = text_file.read()
print(text_data)

# Task 2
# Iterating Through Lines - сount the number of lines in the text

with open ("how_many_lines.txt") as lines_doc:
  for line in lines_doc.readlines():
    print(line)

# Task 3
# Reading a line

with open("just_the_first.txt") as first_line_doc:
  first_line = first_line_doc.readline()
  second_line = first_line_doc.readline()
  third_line = first_line_doc.readline()
print(first_line,second_line,third_line)

# Task 4
# Writing a file
with open("bad_bands.txt", "w") as bad_bands_doc:
  bad_bands_doc.write("A Bad Group")

# Task 5
# Add value to the file (write()) and then read this file (read())
with open("cool_dogs.txt", "a") as cool_dogs_file:
  cool_dogs_file.write("Air Buddy \n")

with open("cool_dogs.txt", "r") as cool_dogs_file:
  text = cool_dogs_file.read()

print(text)

# Task 6
# CSV parsing
with open("logger.csv") as log_csv_file:
  need_to_read = log_csv_file.read()
print(need_to_read)

# Task 7
# Данный код открывает файл "books.csv" в режиме чтения и использует функцию csv.DictReader() для чтения данных из файла в виде словаря, где ключами являются названия столбцов, определенные в первой строке файла, а значениями - соответствующие значения в каждой строке файла.
#
# Аргумент delimiter='@' указывает, что разделителем данных в файле является символ "@".
#
# Затем код проходится по каждой строке файла, извлекает значение поля "ISBN" и добавляет его в список isbn_list. В итоге, код выводит список ISBN-номеров книг, которые были прочитаны из CSV-файла "books.csv".
#
# Таким образом, этот код читает и извлекает данные из CSV-файла, используя словарь для представления каждой строки файла, и создает список ISBN-номеров книг из этого файла.

import csv

with open("books.csv") as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  isbn_list = []
  for key in books_reader:
    isbn_list.append(key['ISBN'])
print(isbn_list)

# Task 8

# Этот код выполняет запись данных из списка access_log в файл CSV с именем "logger.csv".
#
# Первая строка import csv импортирует модуль csv, который позволяет работать с CSV-файлами в Python.
#
# Вторая строка with open("logger.csv", "w") as logger_csv: открывает файл "logger.csv" в режиме записи и создает объект файла logger_csv. Ключевое слово with используется для автоматического закрытия файла после окончания работы с ним.
#
# Третья строка log_writer = csv.DictWriter(logger_csv, fieldnames = fields) создает объект log_writer для записи в CSV-файл, используя метод DictWriter из модуля csv. Этот метод принимает два аргумента: logger_csv, объект файла, и fieldnames, список имен полей (столбцов) в CSV-файле.
#
# Четвертая строка log_writer.writeheader() записывает заголовок (имена столбцов) в CSV-файл.
#
# Пятая строка for element in access_log: начинает итерацию по каждому элементу в списке access_log.
#
# Шестая строка log_writer.writerow(element) записывает каждый элемент в CSV-файл в виде строки, используя метод writerow из объекта log_writer. Каждый элемент должен быть словарем, где ключи словаря соответствуют именам полей (столбцов), определенных в fieldnames, а значения соответствуют значениям в каждой строке CSV-файла.

'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

import csv
with open("logger.csv", "w") as logger_csv:
  log_writer = csv.DictWriter(logger_csv, fieldnames = fields)
  log_writer.writeheader()
  for element in access_log:
    log_writer.writerow(element)





