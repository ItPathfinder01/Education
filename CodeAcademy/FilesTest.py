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

import json
with open("boss_message.json", "w") as boss_message:
  boss_message_dict = {
    "recipient": "The Boss",
    "message": "Mission Success"
    }
  json.dump(boss_message_dict, boss_message)

with open("new_passwords.csv", "w") as new_passwords_obj:
  shall_null_sig = '''
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
'''
  new_passwords_obj.write(shall_null_sig)




