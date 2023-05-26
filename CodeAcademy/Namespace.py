# Task 1

global_variable = 'global'

# Write Checkpoint 1 here:
print (locals())
print (globals())

# Write Checkpoint 2 here:
def divide(num1, num2):
  result = num1/num2
  print(locals())

# Write Checkpoint 3 here:

def multiply(num1, num2):
  product = num1*num2
  print(locals())

print(divide(3,4))
print(multiply(4,50))

print(locals())
