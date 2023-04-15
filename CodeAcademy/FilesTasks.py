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