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
