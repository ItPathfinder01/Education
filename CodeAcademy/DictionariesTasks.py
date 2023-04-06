# Task 1

sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22 }
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}

print(sensors)
print(num_cameras)

# Task 2
# Creation of the dictionary
translations = { "mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch" }

# Task 3

animals_in_zoo = {}

animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0

print(animals_in_zoo)

# Task 4
# Adding many items to the dictionary

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

user_ids.update({"theLooper": 138475, "stringQueen": 85739})

print(user_ids)
# Task 5
#Overwriting the dictionary

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners["Supporting Actress"] = "Viola Davis"

oscar_winners["Best Picture"] = "Moonlight"

# Task 6

rinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)

drinks_to_caffeine = {drinks:caffeine for drinks, caffeine in zip(drinks, caffeine)}

print(drinks_to_caffeine)



