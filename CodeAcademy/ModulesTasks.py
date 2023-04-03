# Task 1

# Import random below:
import random

# Create random_list below:
random_list = []

# Create randomer_number below:
random_list = [random.randint(1, 101) for number in range(101)]

# Print randomer_number below:
randomer_number = random.choice(random_list)

print(randomer_number)

# Task 2

from matplotlib import pyplot as plt
import random

numbers_a = range(1, 13)
numbers_b = random.sample(range(1000), 12)
print(numbers_b)

plt.plot(numbers_a, numbers_b)
plt.show()

# Task 3

from decimal import Decimal

# Fix the floating point math below:
two_decimal_points = Decimal("0.2") + Decimal("0.69")
print(two_decimal_points)

four_decimal_points = Decimal("0.53") * Decimal("0.65")
print(four_decimal_points)

# Task 4
