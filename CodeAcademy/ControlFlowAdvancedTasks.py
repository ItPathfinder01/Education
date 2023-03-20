#Task 1
def in_range(num, lower, upper):
  if num >= lower <= upper:
    return True
  else:
    return False

print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False

#Task 2
def same_name(your_name,my_name):
  if your_name == my_name:
    return True
  return False
  #return False выполняется в любом случае когда в сравнении видно что имена не такие же

print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False

#Task 3
#Always False function
def always_false(num):
  if num > num or num < num:
    return True
  else:
    return False

print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False

#Task 4
def movie_review(rating):
  if rating <= 5:
    return ("Avoid at all costs!")
  elif rating < 9:
    return ("This one was fun.")
  return ("Outstanding!")


print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."

#Task 5
#The function outputs the biggest number
def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  return "It's a tie!"


print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 4, 4))
# should print "It's a tie!"
