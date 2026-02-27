
try:
    f = open("myfile.txt", "r")  # open the file
    line = f.readline()          # read first line
    while line:                  # till the line is not empty
        print(line)              # print this line
        line = f.readline()      # read the next line
finally:
    f.close()


print("******Using WITH option******")
with open("myfile.txt", "r") as f:
    print(f.readline())
    list2 = f.read().split("\n")
    print(list2)

print("******Using For******")
with open("myfile.txt", "r") as f:
    for line in f:
        print(line.strip())
