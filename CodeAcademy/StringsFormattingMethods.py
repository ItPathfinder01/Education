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
