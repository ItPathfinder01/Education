#Task 1
def large_power(base, exponent):
  if base**exponent > 5000:
    return True
  else:
    return False

print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False

#Task 2
def over_budget(budget,food_bill, electricity_bill,internet_bill,rent):
  if budget < food_bill+  electricity_bill + internet_bill + rent:
    return True
  else:
    return False


print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True

#Task 3
def twice_as_large(num1, num2):
    if num1 > num2 * 2:
        return True
    else:
        return False


print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True

#Task 4
def divisible_by_ten(num):
  if num % 10 == 0:
    return True
  else:
    return False


print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False

#Task 5
def not_sum_to_ten(num1, num2):
  if num1 + num2 != 10:
    return True
  else:
    return False

print(not_sum_to_ten(9, -1))
# should print True
print(not_sum_to_ten(9, 1))
# should print False
print(not_sum_to_ten(5,5))
# should print False