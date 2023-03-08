print('''
Task1
''')


def top_tourist_locations_italy():
    first = "Rome"
    second = "Venice"
    third = "Florence"
    fourth = "Verone"
    return first, second, third, fourth


most_popular1, most_popular2, most_popular3, most_popular4 = top_tourist_locations_italy()

# print(most_popular1)
# print(most_popular2)
# print(most_popular3)
# print(top_tourist_locations_italy())

tuple_list = (top_tourist_locations_italy())
# print(tuple)

print(tuple_list[3])

lenght = len(tuple_list)
print(lenght)

print('''
Task2 -пример написания функции для возврата кортежа
''')


def fun():
    str1 = "Happy"
    str2 = "Coding"
    return (str1, str2)


str1, str2 = fun()
print(str1)
print(str2)

print('''
Task3
''')


def natural_numbers(
        numbers=[]):  # тут мы в аргументе просто показываем какую структуру данных функуция принимает как аргумент и название не важно?
    for i in range(1, 40):  # почему ошибка если юзаю []?
        numbers.append(i)
    return numbers


print(natural_numbers())

print('''
Task4
''')


print(student("Nata", 7))
new_student = student("Pasha", 6)
print(new_student)



