import psycopg2
from utilities.configurations import *

# реализация getConnection() метода находится в файле configuration.py
conn = getConnection()
cursor = conn.cursor()


# # создаем таблицу people
# cursor.execute("CREATE TABLE people (id SERIAL PRIMARY KEY, name VARCHAR(50),  age INTEGER)")
# # поддверждаем транзакцию
# conn.commit()
# print("Таблица people успешно создана")
#
# cursor.close()
# conn.close()

# добавляем строку в таблицу people
# cursor.execute("INSERT INTO people (name, age) VALUES ('Sandy', 41)")
# # выполняем транзакцию
# conn.commit()
# print("Данные добавлены")
#
# cursor.close()
# conn.close()

cursor.execute("select * from people")
raws = cursor.fetchall()
print(raws)
# summ = 0
# for raw in raws:
#     summ += raw[2]
# print(summ)

# cursor.execute("UPDATE people SET age =%s WHERE name=%s", ("12", "Tom"))

conn.commit()

conn.close()
