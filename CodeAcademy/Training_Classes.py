# Task 1

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True

    def get_status(self):
        if self.completed:
            return "Выполнена"
        else:
            return "Не выполнена"

    def get_info(self):
        print("Описание задачи:", self.description)
        print("Статус задачи:", self.get_status())


# Пример использования класса "Задача"
task1 = Task("Написать отчет")
task1.get_info()

task1.complete()
task1.get_info()

Task 2

class Lightbulb:
    def __init__(self, bulb_type, bulb_state):
        self.bulb_type = bulb_type
        self.bulb_state = bulb_state

    def bulb_toggle(self):
        if self.bulb_state == "turned_off":
            self.bulb_state = "turned_on"
        elif self.bulb_state == "turned_on":
            self.bulb_state = "turned_off"
        else:
            raise ValueError("Invalid bulb state")

    def check_the_bulb(self):
        return(f"{self.bulb_type} is {self.bulb_state}")


NeonBulb = Lightbulb("Neon bulb", "turned_off")

NeonBulb.bulb_toggle()
print(NeonBulb.bulb_state)
NeonBulb.bulb_toggle()
print(NeonBulb.bulb_state)

# Task 2

class Car:
    def __init__(self, model, manufactured_in, max_speed, car_cost, fuel_consamption):
        self.model = model
        self.manfactued_in = manufactured_in
        self.max_speed = max_speed
        self.car_cost = car_cost
        self.fuel_consamption = fuel_consamption
        self.upgrades = []

    def __repr__(self):
        upgrades_info = "Upgrades: " + ", ".join(self.upgrades) if self.upgrades else "No upgrades"
        return f"{self.model}, manufactered in {self.manfactued_in }\nMax speed is {self.max_speed} km/h\nFuel consumption is {self.fuel_consamption} litres per 100 km.\nCar cost is {self.car_cost} US$.\n{upgrades_info}"

    def engine_upgrade(self):
        self.max_speed += 50
        self.car_cost += 2500
        self.fuel_consamption += 2
        self.upgrades.append("Engine upgrade")
        return (f"We have upgraded the engine, max speed increased by 50 km/h and now {self.max_speed} km/h. The price of the car now {self.car_cost} US$. Fuel consamption is now {self.fuel_consamption} litres per 100 km.")

    def tires_change(self):
        self.max_speed += 20
        self.car_cost += 500
        self.fuel_consamption += 0.5
        self.upgrades.append("Tires upgrade")
        return (f"After installation of a new tires max speed is {self.max_speed}. Fuel consumption is {self.fuel_consamption}litres per 100 km and the car costs now {self.car_cost}.")

    def car_params(self):
        upgrades_info = "Upgrades: " + ", ".join(self.upgrades) if self.upgrades else "No upgrades"
        return f"{self.model}, manufactered in {self.manfactued_in }\nMax speed is {self.max_speed} km/h\nFuel consumption is {self.fuel_consamption} litres per 100 km.\nCar cost is {self.car_cost} US$.\n{upgrades_info}"




Renault_Logan = Car("Renault Logan",2015,140,5000,8)
Renault_Logan.tires_change()
Renault_Logan.engine_upgrade()
print(Renault_Logan)



