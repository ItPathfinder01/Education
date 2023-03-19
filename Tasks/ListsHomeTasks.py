# Task 1

def int_numbers():
    figure = input("Введите свой лист: ")
    return figure


def even_numbers():
    figure = int_numbers()
    new_list = [int(element) for element in figure if int(element) % 2 == 0]

    print(new_list)

even_numbers()
