# Task 1
# Reading files
with open("welcome.txt") as text_file:
  text_data = text_file.read()
print(text_data)

# Task 2
# Iterating Through Lines - сount the number of lines in the text

with open ("how_many_lines.txt") as lines_doc:
  for line in lines_doc.readlines():
    print(line)

# Task 3
# Reading a line

with open("just_the_first.txt") as first_line_doc:
  first_line = first_line_doc.readline()
  second_line = first_line_doc.readline()
  third_line = first_line_doc.readline()
print(first_line,second_line,third_line)

# Task 4
# Writing a file
with open("bad_bands.txt", "w") as bad_bands_doc:
  bad_bands_doc.write("A Bad Group")

# Task 5
# Add value to the file (write()) and then read this file (read())
with open("cool_dogs.txt", "a") as cool_dogs_file:
  cool_dogs_file.write("Air Buddy \n")

with open("cool_dogs.txt", "r") as cool_dogs_file:
  text = cool_dogs_file.read()

print(text)

# Task 6
# CSV parsing
with open("logger.csv") as log_csv_file:
  need_to_read = log_csv_file.read()
print(need_to_read)

