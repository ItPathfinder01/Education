class Invasion:
    def __init__(self, unit_name, quantity, weapon, commander):
        self.unit_name = unit_name
        self.quantity = quantity
        self.weapon = weapon
        self.commander = commander

    def __repr__(self):
        vehicle_info = '\n'.join(f'{vehicle}: {quantity}' for vehicle, quantity in self.weapon.items())
        return f'{self.unit_name} - {self.quantity} of soldiers are available for invasion\nHere are available vehicles:\n{vehicle_info}\nThe commander is {self.commander}.'


cadian_weapon = {
    "Leman russ": 1000, "Chimera": 100000, "Basilisk": "2000", "Hellhound": 5000
}

valhavvan_weapon = {
    "Sentinel": 5000, "Centaur": 4000, "Valkyrie": 3000, "Vulture": 1000
}

krieg_weapon = {
    "Griffon": 10000, "Bombard": 5000, "Leman russ": 4000, "Colossus": 1000
}

cadian_forces = Invasion("2nd Cadian regiment", 1000000, cadian_weapon, "Sebastian Yarrick")
valhallan_forces =Invasion("54th Valhallan regiment", 500000,valhavvan_weapon, "Ciaphas Cain"  )
krieg_forces = Invasion("83rd Death Korps of Krieg regiment", 2000000, krieg_weapon, "Colonel Jurten")


print(valhallan_forces)
