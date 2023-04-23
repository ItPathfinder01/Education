# Task 1
# Define the class
class Facade:
  pass

facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)

# Task 2
class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."

# Task 3
class Circle:
  pi = 3.14
  def area(self, radius):
    return Circle.pi * radius ** 2    # Обратились к переменной pi через имя класса Circle.pi

circle = Circle()   # создали объект класса Circle
pizza_area = circle.area(12 / 2)
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)

print(pizza_area,teaching_table_area,round_room_area)


# Task 4
# В этом коде создается класс Circle, который имеет атрибут класса pi, равный 3.14. Затем определяется конструктор __init__, который принимает единственный аргумент diameter и выводит сообщение на экран, содержащее значение диаметра.
#
# Затем создается экземпляр класса Circle с аргументом 36 и сохраняется в переменную teaching_table. При создании этого экземпляра, конструктор __init__ вызывается с аргументом 36, и на экран выводится сообщение "New circle with diameter: 36".
#
# Обычно конструкторы используются для инициализации атрибутов объекта, но в данном случае конструктор просто выводит сообщение на экран, чтобы показать, что экземпляр был создан.
#
class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print('New circle with diameter: {}'.format(diameter))


teaching_table = Circle(36)
