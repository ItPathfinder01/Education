#Task 1
# Добавляем в конец списка количество символов в списке
def append_size(my_list):
  list_lenghs = len(my_list)
  my_list.append(list_lenghs)
  return my_list


print(append_size([23, 42, 108]))

#Task 2
# Складываем вместе два последних элемента списка и цикл делает это три раза
def append_sum(my_list):
  for runner in range(3):
   runner = my_list[-2] + my_list[-1]
   my_list.append(runner)
  return my_list

print(append_sum([1, 1, 2]))

#Task 3
def larger_list(my_list1, my_list2):
  firstLenght = len(my_list1)
  secondLenght = len(my_list2)
  if firstLenght >= secondLenght:
    return my_list1[-1]
  elif firstLenght < secondLenght:
    return my_list2[-1]


print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

#Task 4
def larger_list(my_list1, my_list2):
  if len(my_list1) >= len(my_list2):
    return my_list1[-1]
  return my_list2[-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

#Task 5

def combine_sort(my_list1, my_list2):
  combined_list = my_list1 + my_list2
  combined_list.sort()
  return combined_list

#Task 5.1
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

def combined_sort_new(my_list1, my_list2):
    return sorted(my_list1 + my_list2)

print(combined_sort_new([4, 10, 2, 5], [-10, 2, 5, 10]))

