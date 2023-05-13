# Task 1
class Employee:
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print(f"My id is {self.id}")

class User:
  def __init__(self, username, role="Customer"):
    self.username = username
    self.role = role

  def say_user_info(self):
    print("My username is {}".format(self.username))
    print("My role is {}".format(self.role))

class Admin(Employee,User): # Multiple Inheritance of Employee and User method
  def __init__(self):
        super().__init__()
        User.__init__(self, self.id, "Admin")  # Вызываю конструктор класса юзер. (self.id, унаследованный от класса Employee,тут является параметром username) а как параметр role, передаётся "Admin"

  def say_id(self):    # Override the method with another output
    super().say_id()   # Super method allows to use the logic from Employee class
    print("I am an Admin")

class Manager(Admin):  # Multiple inheritance: Admin inherits-Employee and then Manager inherits Admin
  def say_id(self):
    super().say_id()   # Super method allows to use the logic from Employee class
    print("They are in charge")

e1 = Employee()
e2 =Admin()
e3 = Manager()

e1.say_id()
e2.say_id()
e3.say_user_info()

# Task 2 Plymorphism. Here objects of different classes are using the same method

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
    super().say_id()
    print("I am an admin.")

class Manager(Admin):
  def say_id(self):
    super().say_id()
    print("I am in charge!")

user1 = Employee()
user2 = Admin()
user3 = Manager()

meeting = [user1, user2, user3]

for user in meeting:
  user.say_id()

# Task 3 __ADD__ dunder method works as + operator

class Employee():
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1


class Meeting:
    def __init__(self):
        self.attendees = []

    def __len__(self):
        return len(self.attendees)

    def __add__(self, employee):
        print("ID {} added.".format(employee.id))
        self.attendees.append(employee)

    # Write your code


e1 = Employee()
e2 = Employee()
e3 = Employee()
m1 = Meeting()
m1 + e1
m1 + e2
m1 + e3
print(len(m1))

# Task 4 Abstraction

from abc import ABC, abstractmethod

class AbstractEmployee(ABC):
  new_id = 1
  def __init__(self):
    self.id = AbstractEmployee.new_id
    AbstractEmployee.new_id += 1

  @abstractmethod
  def say_id(self):
    pass

# Write your code below
class Employee(AbstractEmployee):
    def say_id(self):
      print(f"The id is {self.id}")

e1 = Employee()
e2 = Employee()
e1.say_id()
e2.say_id()

# Task 5 Encapsulation

class Employee():
    def __init__(self):
        self.id = None
        self._id = None
        self.__id = None     # Name mangling mechanism is applied to this attribute, as a result we will see _Classname__id

e = Employee()
print(dir(e))                # dir() returns all attributes of the current module or object


# Task 6 Encapsulation

class Employee():
    new_id = 1

    def __init__(self, name=None):
        self.id = Employee.new_id
        Employee.new_id += 1
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def del_name(self):
        del self._name
        print("The name deleted")


e1 = Employee("Maisy")
e2 = Employee()

e1 = Employee("Maisy")
e2 = Employee()
print(e1.get_name())

e2.set_name("Fluffy")
print(e2.get_name())

e2.del_name()
print(e2.get_name())

