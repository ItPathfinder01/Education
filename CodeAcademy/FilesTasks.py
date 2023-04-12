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

