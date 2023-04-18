# Этот код импортирует модуль csv, открывает файл "passwords.csv" в режиме чтения, используя open(), и использует csv.DictReader() для чтения содержимого файла в словарь. Затем он создает пустой список compromised_users.
# Затем происходит итерация по каждой строке файла CSV с помощью цикла for, который обрабатывает каждую строку как словарь. Из каждой строки извлекается значение, соответствующее ключу "Username" с помощью обращения к словарю через ключ. Это значение добавляется в список compromised_users.
# После прохождения через все строки файла CSV, код выводит список compromised_users, содержащий все имена пользователей (из столбца "Username"), чьи учетные записи были скомпрометированы и сохранены в файле "passwords.csv".

import csv

compromised_users = []

with open("passwords.csv") as password_file:
  password_csv = csv.DictReader(password_file)
  for password_row in password_csv:
    compromised_users.append(password_row["Username"])
  # print(compromised_users)


with open("compromised_users.txt", "w") as compromised_user_file:
  for user in compromised_users:
    compromised_user_file.write(user)




