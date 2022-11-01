import fileinput
import re
total = int(input("Enter total number of files: "))
list_of_files = []
count = False
count_files = 0
for i in range(total):
    path = input("Enter File Path:")
    list_of_files.append(path)

check = input("Enter word to check: ")
for i in range(total):
    for line in fileinput.input(files=list_of_files[i]):
        altered_line = re.sub(',', '', line)
        contents = altered_line.split()
        if check in contents:
            count = True
    if count:
        count_files += 1
        count = False

print(f"{count_files}/{total}")
print(count_files * 100 / total)
