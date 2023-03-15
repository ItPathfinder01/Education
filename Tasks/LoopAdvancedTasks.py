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
