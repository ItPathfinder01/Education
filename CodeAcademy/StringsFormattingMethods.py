# Task 1

poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
print(poem_title)
print(poem_title_fixed)

poem_author_fixed = poem_author.upper()
print(poem_author)
print(poem_author_fixed)

# Task 2

line_one = "The sky has given over"
line_one_words = line_one.split()
print(line_one_words)

# Task 3
# Split - разделяет строки в список
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")
print(author_names)

author_last_names = []
for name in author_names:
    author_last_names.append(name.split()[-1])

print(author_last_names)

# Task 4
# \ используется для переноса строки
spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""


spring_storm_lines = spring_storm_text.split("\t")
print(spring_storm_lines)

spring_storm_lines = spring_storm_text.split("\n")
print(spring_storm_lines)

# Task 5
# Join - соединяет строки с разделителем пробелами
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = (" ".join(reapers_line_one_words))
print (reapers_line_one)

# Task 6

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = ("\n".join(winter_trees_lines))
print (winter_trees_full)

# Task 7

def clean_up(*list_to_clean):
  clean_list = []
  for cleaner in list_to_clean:
    for item in cleaner:
      clean_item = item.strip()
      clean_list.append(clean_item)
  return clean_list

def need_to_join(a_list):
  joined_result = " ".join(a_list)
  return joined_result

after_clean = clean_up(['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    '])

after_join = need_to_join(after_clean)

print(after_join)

# Task 7.1

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']


love_maybe_lines_stripped = []

for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())

love_maybe_full = '\n'.join(love_maybe_lines_stripped)

print(love_maybe_full)

# Task 8
# replace - принимает два параметра и меняет первый на второй (можно использовать для замены в тексте)
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""

toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer")
print (toomer_bio_fixed)

# Task 9

the_list = ["a","b","c","d","e","f","j"]
if "w" in the_list:
  print("It is there")
else:
  print("It is not there")

# Task 10
#find() - поиск индекса первого вхождения элемента в списке
god_wills_it_line_one = "The very earth will disown you"

disown_placement = "The very earth will disown you".find("disown")
print (disown_placement)

# Task 11
# format() - это метод строк в Python, который позволяет вставлять значения переменных внутрь строки. Он возвращает новую строку, которая является копией исходной строки с замененными значениями переменных.
def poem_title_card(title, poet):
  return "The poem \"{}\" is written by {}.".format(title, poet)


print(poem_title_card("I Hear America Singing", "Walt Whitman"))

# Task 12

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(title = title, author = author, original_work = original_work, publishing_date = publishing_date )
  return poem_desc

author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

my_beard_description = poem_description(publishing_date, author, title, original_work)
print(my_beard_description)

# Task 13



