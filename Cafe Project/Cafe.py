print("Welcome to Ichiraku Ramen")

bouillon_options = ["shoyu", "shio", "miso"]
meat_options = ["chicken", "pork", "beef", "turkey"]
addition_options = ["egg", "mushrooms", "tofu", "vegetables", "bacon", "kimchi"]

print("Ichiraku Ramen bouillons")
print("------------------")
i = 1
for b in bouillon_options:
    print(i, b)
    i += 1
bouillon = input("Choose the bouillon ")

print("Ichiraku Ramen meat options")
print("------------------")
i = 1
for m in meat_options:
    print(i, m)
    i += 1
meat = input("Choose your meat ")


print("Ichiraku Ramen additions")
print("------------------")
i = 1
for a in addition_options:
    print(i, a)
    i += 1
addition = input("Choose the additions ")

print(bouillon_options[int(bouillon)-1])
print(meat_options[int(meat)-1])
print(addition_options[int(addition)-1])