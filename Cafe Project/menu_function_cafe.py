def menu(choices, title="Ichiraku Ramen", prompt="Choice the option "):
    print(title)
    print(len(title) * '_')
    i = 1
    for c in choices:
        print(i, c)
        i += 1

    while True:
        choice = input(prompt)
        allowed_answers =[]
        for a in range(1, len(choices)+1):
            allowed_answers.append(str(a))
        if choice in allowed_answers:
            answer = choices[int(choice) -1]
            break
        else:
            print("Choice 1,2 or 3")
            answer = " "
    return answer


bouillon_options = ["shoyu", "shio", "miso"]
meat_options = ["chicken", "pork", "beef", "turkey"]
addition_options = ["egg", "mushrooms", "tofu", "vegetables", "bacon", "kimchi"]
bouillon = menu(bouillon_options, "Ichiraku Ramen", "Choice the bouillon: ")
meat = menu(meat_options, "Ichiraku Ramen", "Choice the meat: ")
addition = menu(addition_options, "Ichiraku Ramen", "Choice the addition: ")

print("Your order:")
print("Your bouillon is:", bouillon)
print("Your meat is:", meat)
print("Your addition is:", addition)
print("Thank you for the order!")

