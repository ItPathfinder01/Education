class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return (f"{self.name} menu is available from {self.start_time} till {self.end_time}.")

    def calculate_bill(self, purchased_items):
        bill = 0
        for purchased_item in purchased_items:
            if purchased_item in self.items:
                bill += self.items[purchased_item]
        return (f"The price of the meal is {bill}$.")


# Brunch menu

brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
    'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

brunch_menu = Menu("Brunch", brunch_items, 1100, 1600)
# Early_bird menu

early_bird_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

early_bird_menu = Menu("Early bird", early_bird_items, 1500, 1800)
# Dinner menu

dinner_items = {
    'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

dinner_menu = Menu("Dinner", dinner_items, 1700, 2300)
# Kids menu

kids_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids_menu = Menu("Kids", kids_items, 1100, 2100)

print(dinner_menu)

print(kids_menu.calculate_bill(["chicken nuggets", "apple juice"]))


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return self.address

    def available_menus(self, time):
        current_menu = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                current_menu.append(menu)
        return current_menu


menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

flagship_store = Franchise("1232 West End Road", menus)

new_installement = Franchise("12 East Mulberry Street", menus)

print(flagship_store.available_menus(1700))


class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


Basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installement])

arepas_items = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

Arepas_menu = Menu("Arepa", arepas_items, 1000, 2000)

Arepas_place = Franchise("189 Fitzgerald Avenue", [Arepas_menu])

print(Arepas_place.menus)

business_arepa = Business("Take a' Arepa", [Arepas_place])

print(business_arepa.franchises)
