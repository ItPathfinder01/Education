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
