# Task 1
class Employee:
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print(f"My id is {self.id}")

class Admin(Employee): # Inherited Employee method
  def say_id(self):    # Override the method with another output
    super().say_id()   # Super method allows to use the logic from Employee class
    print("I am an Admin")

e1 = Employee()
e2 = Employee()
e3 = Employee()
e4 = Admin()

e1.say_id()
e2.say_id()
e3.say_id()
e4.say_id()
# Task 2
