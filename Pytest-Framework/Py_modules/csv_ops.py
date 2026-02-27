import csv

with open("myfile.csv", mode="r") as file:
    csvFile = csv.reader(file)
    for item in csvFile:
        print(item)

print("=====================")
print("=====================")

with open("myfile.csv", mode="r") as file:
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        print(lines)

print("=====================")

rows = []
with open("myfile.csv", mode="r") as file:
    csvFile = csv.reader(file)
    header = next(csvFile)
    for item in csvFile:
        rows.append(item)

print(rows)
for row in rows:
    print(row)


