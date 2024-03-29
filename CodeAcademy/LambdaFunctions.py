# Лямбда-функции, также известные как анонимные функции, позволяют создавать простые функции без необходимости использования
# ключевого слова def.Они обычно используются в тех случаях, когда требуется определить небольшую функцию на месте ее вызова. Вот
# базовый синтаксис лямбда-функций в Python

# lambda arguments: expression
#
# lambda: ключевое слово, указывающее на создание лямбда-функции.
# arguments: аргументы функции, которые принимает лямбда-функция.
# expression: выражение, которое выполняется и возвращается как результат работы лямбда-функции.

# Пример 1: Возведение числа в квадрат
# square = lambda x: x**2
# print(square(5))  # Вывод: 25
#
# Пример 2: Сложение двух чисел
# addition = lambda x, y: x + y
# print(addition(3, 4))  # Вывод: 7
#
# # Пример 3: Проверка, является ли число четным
# is_even = lambda x: x % 2 == 0
# print(is_even(6))  # Вывод: True

# Task 1

grade_list = [3.5, 3.7, 2.6, 95, 87]

updated_grade_list = list(map(lambda x: x * 25 if x <= 4 else x, grade_list))

print(updated_grade_list)

