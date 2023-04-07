# Task 1

first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  new_account = first_name[:3] + last_name[:3]
  return new_account
  print(new_account)

account_generator(first_name, last_name)

# Task 2

first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  temporary_pass = first_name[2:] + last_name[4:]
  return temporary_pass

temp_password = password_generator(first_name, last_name)

# Task 3

first_name = "Bob"
last_name = "Daily"

fixed_first_name = "R" + first_name[1:]
print(fixed_first_name)
fixed_last_name = "K" + last_name[1:]
print(fixed_last_name)

# Task 4

def get_length(word):
  counter = 0
  for figure in word:
    counter += 1
  return counter


print(get_length("SdohniPutin"))

# Task 5

def common_letters(string_one, string_two):
  common_list = []
  for letter in string_one:
    if letter in string_two and not letter in common_list:
      common_list.append(letter)
  return common_list


print(common_letters("manhattan", "san francisco"))

# Task 6

def username_generator(first_name, last_name):
  username = first_name[:3] + last_name[:4]
  if len(first_name) < 3 or len(last_name) < 4:
    return last_name + first_name
  return username

print(username_generator("Ab", "Simpson"))

def password_generator(user_name):
  password = ""
  for index in range(0, len(user_name)):
     password += user_name[index-1]
  return password

print(password_generator("Tania"))




