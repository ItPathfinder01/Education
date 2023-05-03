# Task 1

def sum_values(my_dictionary):
  counter = 0
  for value in my_dictionary.values():
    counter += value
  return counter



print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

# Task 2
def sum_even_keys(my_dictionary):
  keys_summ = 0
  for figure in my_dictionary.keys():
    if figure %2 == 0:
      keys_summ += my_dictionary[figure]
  return keys_summ



print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

# Task 3
