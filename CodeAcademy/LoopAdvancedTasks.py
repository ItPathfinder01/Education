# Task 1

def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for element in lst1:
        sum1 += element
    for element in lst2:
        sum2 += element
    if sum1 > sum2:
        return lst1
    return lst2


print(larger_sum([1, 9, 5], [2, 3, 7]))


# Task 2

def over_nine_thousand(lst):
    total = 0
    for element in lst:
        total += element
        if total > 9000:
            break
    return total


print(over_nine_thousand([8000, 900, 120, 5000]))


# Task 3

def max_num(nums):
    max_value = nums[0]
    for element in nums:
        if element > max_value:
            max_value = element
            continue
    return max_value


print(max_num([50, -10, 0, 75, 20]))
print(max_num([-50, -20]))


# Task 4
def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# Task 5

def reversed_list(lst1, lst2):
    if lst1 == list(reversed(lst2)):
        return True
    return False

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

