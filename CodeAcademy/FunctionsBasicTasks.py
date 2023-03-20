# Task 1

def tenth_power(num):
    return num ** 10


print(tenth_power(1))
print(tenth_power(0))
print(tenth_power(2))


# Task 2
def square_root(num):
    return num ** 0.5


print(square_root(16))
print(square_root(100))


# Task 3

def win_percentage(wins, looses):
    total_games = wins + looses
    win_ratio = wins / total_games
    return win_ratio * 100


print(win_percentage(5, 5))

print(win_percentage(10, 0))


# Task 4

def average(num1, num2):
    average_number = (num1 + num2) / 2
    return average_number


print(average(1, 100))

print(average(1, -1))


# Task 5

def remainder(num1, num2):
    return (num1 * 2) % (num2 / 2)


print(remainder(15, 14))
print(remainder(9, 6))

