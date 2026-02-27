def menu(choices, title="Ichiraku Ramen", prompt="Choice the option "):
    print(title)
    print(len(title) * '_')
    i = 1
    for c in choices:
        print(i, c)
        i += 1

    while True:
        choice = input(prompt)
        allowed_answers = []
        for a in range(1, len(choices)+1):
            allowed_answers.append(str(a))
        allowed_answers.append("x")
        allowed_answers.append("X")
        if choice in allowed_answers:
            if choice == "X" or choice == "x":
                answer = ""
                break
            else:
                answer = choices[int(choice) - 1]
                break

        else:
            print("Enter number from 1 to ", len(choices), "or X if you don't want it")
            answer = " "
    return answer



def read_menu(filename):
    file = open(filename)
    temp = file.readlines()
    result = []
    for char in temp:
        new_item = char.strip()
        result.append(new_item)
    return result

bouillons = read_menu("bouillons_options.txt")
meats = read_menu("meat_options.txt")
additions = read_menu("addition_options.txt")


bouillon = menu(bouillons, "Ichiraku Ramen", "Choice the bouillon: ")
meat = menu(meats, "Ichiraku Ramen", "Choice the meat: ")
addition = menu(additions, "Ichiraku Ramen", "Choice the addition: ")

print("Your order:")
print("Your bouillon is:", bouillon)
print("Your meat is:", meat)
print("Your addition is:", addition)
print("Thank you for the order!")

