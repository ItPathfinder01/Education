import json

# file = '''{
#     "name": "Tatooine",
#     "rotation_period": "23",
#     "orbital_period": "304",
#     "diameter": "10465",
#     "climate": "arid",
#     "gravity": "1 standard",
#     "terrain": "desert",
#     "surface_water": "1"
# }'''


# Loads method parses jsom string and returns dictionary

# new_file = json.loads(file)
# print(type(new_file))
# print(new_file)
#
# container_key = []
# container_value = []
#
# for item in new_file:
#     container_key.append(item)
#     container_value.append(new_file[item])
#
#
# print(container_key)
# print(container_value)

# Parsing the info from Json file using json.load function

with open("/Users/alexkibryk/Desktop/JustFile.json", 'r') as test_file:
    file_to_read = json.load(test_file)

# print(file_to_read["terrain"])

with open("/Users/alexkibryk/Desktop/NabuFile.json", 'r') as test_file2:
    file_to_read2 = json.load(test_file2)

assert file_to_read == file_to_read2

