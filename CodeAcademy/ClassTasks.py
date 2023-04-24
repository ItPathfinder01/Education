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

# Task 5
import random
class HeroesStuff:
  def __init__(self, power1, power2,  weakness):
    self.power1 = power1
    self.power2 = power2
    self.weakness = weakness

super_powers = ["Invisibility", "Super strength", "Telekinesis", "Flight", "X-ray vision", "Super speed", "Immortality"]
super_weaknesses = ["Loud noise", "Kryptonite", "Water", "Fire", "Electricity", "Iron", "Light sun"]

while True:
    power1, power2 = random.sample(super_powers, 2)
    if power1 != power2:
        break

super_ability = HeroesStuff(power1, power2, random.choice(super_weaknesses))
print("Your first super power is " + super_ability.power1 + ", your second super power is " + super_ability.power2 + " and your weakness is " + super_ability.weakness)

# Task 6
# getattr() - это встроенная функция в Python, которая возвращает значение атрибута объекта по его имени. Она принимает два аргумента: объект и имя атрибута.
# hasattr() - это встроенная функция в Python, которая проверяет, содержит ли объект атрибут с заданным именем. Она принимает два аргумента: объект и имя атрибута.
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
  if hasattr(element, "count"):
    print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute :(")

# Task 7

class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter / 2

  def circumference(self):
    return 2 * self.pi * self.radius

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

