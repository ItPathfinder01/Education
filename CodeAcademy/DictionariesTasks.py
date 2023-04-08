# Task 1

sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}

print(sensors)
print(num_cameras)

# Task 2
# Creation of the dictionary
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}

# Task 3
# Adding new stuff or editing xisting
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
# Overwriting the dictionary

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone",
                 "Animated Feature": "Zootopia"}

oscar_winners["Supporting Actress"] = "Viola Davis"

oscar_winners["Best Picture"] = "Moonlight"

# Task 6

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)

drinks_to_caffeine = {drinks: caffeine for drinks, caffeine in zip(drinks, caffeine)}

print(drinks_to_caffeine)

# Task 7

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

zipped = zip(songs, playcounts)

plays = {songs: playcounts for songs, playcounts in zip(songs, playcounts)}

plays["Purple Haze"] = 1
plays["Respect"] = 94

# print(plays)

library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)

# Task 8
# Getting dictionary value by it's key
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"],
                   "earth": ["Taurus", "Virgo", "Capricorn"], "air": ["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"])
print(zodiac_elements["fire"])

# Task 9

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"],
                   "earth": ["Taurus", "Virgo", "Capricorn"], "air": ["Gemini", "Libra", "Aquarius"]}

key_to_check = "enegry"
if key_to_check in zodiac_elements:
    print(zodiac_elements["energy"])

# Task 10
#get values from from dictionary. If the key or value doesn exist returns predifined value
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)

stack_id = user_ids.get("superStackSmash",100000)
print(stack_id)

# Task 11
# Add values by key to a variable and then remove from the dictionary using pop() function
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)

