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

# Task 2
