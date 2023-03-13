# Task 1 Solved via list comprehension
def divisible_by_ten(nums):
    counter = 0
    final_counter = [counter for counter in nums if counter % 10 == 0]
    return len(final_counter)


print(divisible_by_ten([20, 25, 30, 50, 35, 40]))


# Solved via regular loop
def divisible_by_ten(nums):
    count = 0
    for number in nums:
        if (number % 10 == 0):
            count += 1
    return count


print(divisible_by_ten([20, 25, 30, 50, 35, 40]))

# Task 2
def add_greetings(names):
    new_list = ["Hello, " + checker for checker in names]
    return new_list


print(add_greetings(["Owen", "Max", "Sophie"]))

# Task 3 List comprehension

def add_greetings(names):
    new_list = ["Hello, " + checker for checker in names]
    return new_list


print(add_greetings(["Owen", "Max", "Sophie"]))

# Solved via regular loop plus append function
def add_greetings(names):
    new_list = []
    for name in names:
        new_list.append("Hello, " + name)
    return new_list
print(add_greetings(["Owen", "Max", "Sophie"]))

# Task 3

def delete_starting_evens(lst):
 new_list =[]
 for checker in lst:
     if checker % 2 == 1:
      new_list = lst.remove(checker)
     elif checker % 2 == 0:
 return new_list


print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
