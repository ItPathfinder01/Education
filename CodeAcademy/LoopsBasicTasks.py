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
    while len(lst) > 0 and lst[0] % 2 == 0:
        lst = lst[1:]
    return lst

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

# Task 3.1

def delete_starting_evens(lst):
  index = 0
  while index < len(lst):
      element = lst[index]
      if element % 2 == 0:
          index += 1
          continue
      return lst[index:]
  return []


print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

# Task 3.2

def delete_starting_evens(lst):
    for element in lst:
        if element % 2 == 1:
            return lst[lst.index(element):]
    return []


print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

#Task 4

def odd_indices(lst):
    new_list = [lst[index] for index in range(len(lst)) if index % 2 == 1]
    return new_list

print(odd_indices([4, 3, 7, 10, 11, -2]))

# Task 5

def exponents(bases, powers):
  new_list = []
  for baseElement in bases:
    for powersElement in powers:
      new_list.append( baseElement ** powersElement )
  return new_list

print(exponents([2, 3, 4], [1, 2, 3]))




