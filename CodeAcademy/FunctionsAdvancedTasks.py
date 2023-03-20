# Task 1

def first_three_multiples(num):
    print(num * 1)
    print(num * 2)
    print(num * 3)
    return num * 3


first_three_multiples(10)

first_three_multiples(0)


# Task 2

def tip(total, percentage):
    tip_amount = (total * percentage) / 100
    return tip_amount


print(tip(10, 25))
print(tip(0, 100))


# Task 3
def introduction(first_name, last_name):
    return (last_name + ", " + first_name + " " + last_name)


print(introduction("James", "Bond"))
print(introduction("Maya", "Angelou"))

# Task 4

def dog_years(name, age):
  return name + ", " + "you are " + str(age * 7) + " years old in dog years"


print(dog_years("Lola", 16))

print(dog_years("Baby", 0))

# Task 5

def lots_of_math(a,b,c,d):
  ab_sum = a + b
  cd_minus = c - d
  prefinal_result = ab_sum * cd_minus
  fourth = prefinal_result % a
  print(ab_sum)
  print(cd_minus)
  print(prefinal_result)
  return fourth




print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0


