# Task 1

def int_numbers():
    figure_str = input("Введите лист чисел через запятую: ")
    return figure_str.split(",")


def even_numbers():
    figure = int_numbers()
    new_list = [int(element) for element in figure if int(element) % 2 == 0]

    print("Ответ: ", new_list)

even_numbers()

