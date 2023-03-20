#Task 1
def every_three_nums(start):
    list = []
    for checker in range(start, 101, 3):
        list.append(checker)
    return list


print(every_three_nums(90))

#Task 2
def remove_middle(my_list, start, end):
 for index in range(start, end + 1):
    my_list.pop(start)
 return my_list

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))


#Task 3
# промежуточное длинное решение, после анализа понял как можно сократить - Task 3.1
def more_frequent_item(my_list, item1, item2):
  firstItem = my_list.count(item1)
  secondItem = mlist.count(item2)
  if firstItem >= secondItem:
      return firstItem
  return secondItem

#Task 3.1
def more_frequent_item(my_list, item1, item2):
  if my_list.count(item1) >= my_list.count(item2):
   return item1
  return item2

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

#Task 4

def double_index(my_list, index):
  # Checks to see if index is too big
  if index >= len(my_list):
    return my_list
  else:
    # Gets the original list up to index
    my_new_list = my_list[0:index]
 # Adds double the value at index to the new list
  my_new_list.append(my_list[index]*2)
  #  Adds the rest of the original list
  my_new_list = my_new_list + my_list[index+1:]
  return my_new_list
print([1, 2, 3, 4], 2)

#Task 5
def middle_element(my_list):
 mid_element1 = len(my_list) // 2
 position1 = my_list[mid_element1]
 position2 = my_list[mid_element1 - 1]
 if len(my_list) % 2 == 0:
    return (position1 + position2) / 2
    return position1

print(middle_element([5, 2, -10, -4, 4, 5]))





