# Task 1

first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  new_account = first_name[:3] + last_name[:3]
  return new_account
  print(new_account)

account_generator(first_name, last_name)