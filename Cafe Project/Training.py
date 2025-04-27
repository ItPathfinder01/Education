# import random
#
# x = random.randint(1, 10)
#
# while True:
#     i = int(input("Guess the number: "))
#     if i == x:
#         print("Correct")
#         break
#     print("Try again")
list = ["One", "Two", "Three", "Four", "Five"]
new_list =[]
for x in range(1, len(list)+1):
    new_list.append(str(x))
    print(new_list)



