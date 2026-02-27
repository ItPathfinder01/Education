def clean_menu(filename):
    file = open(filename)
    temp = file.readlines()
    result = []
    for char in temp:
        new_item = char.strip()
        result.append(new_item)
    return result

bouillons = clean_menu("bouillons_options.txt")
print(bouillons)
meat = clean_menu("meat_options.txt")
print(meat)
additions = clean_menu("addition_options.txt")
print(additions)