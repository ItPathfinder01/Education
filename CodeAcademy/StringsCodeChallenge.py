# Task 1

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
  uniques = 0
  for letter in letters:
    if letter in word:
      uniques += 1
  return uniques

print(unique_english_letters("mississippi"))

print(unique_english_letters("Apple"))

# Task 2
def count_char_x(word, x):
  counter = 0
  for letter in word:
    if letter == x:
      counter += 1
  return counter

print(count_char_x("mississippi", "s"))

print(count_char_x("mississippi", "m"))

# Task 3

def count_multi_char_x(word, x):
  counter = word.split(x)
  return(len(counter) -1)

print(count_multi_char_x("mississippi", "iss"))

print(count_multi_char_x("apple", "pp"))

# Task 4
def substring_between_letters(word, start, end):
  start_index = word.find(start)
  end_index = word.find(end)
  if start_index > -1 and end_index > -1:
    return(word[start_index+1:end_index])
  return word




print(substring_between_letters("apple", "p", "e"))

print(substring_between_letters("apple", "p", "c"))

# Task 5
def x_length_words(sentence, x):
  numbers = sentence.split(" ")
  for number in numbers:
    if len(number) < x:
      return False
    return True

print(x_length_words("i like apples", 2))

print(x_length_words("he likes apples", 2))

# Task 6

def check_for_name(sentence, name):
  if name.lower() in sentence.lower():
    return True
  return False


print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

# Task 7

def every_other_letter(word):
  string =""
  for letter in range(0, len(word),2):
    string += word[letter]
  return string




print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print

# Task 8
def reverse_string(word):
  reverse = ""
  for letter in range(len(word)-1, -1, -1):
    reverse += word[letter]
  return reverse



print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

# Task 9
def make_spoonerism(word1, word2):
  return word2[0]+word1[1:]+" "+word1[0]+word2[1:]


print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a

# Task 10
def add_exclamation(word):
  while (len(word) < 20):
    word += ("!")
  return word


print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
