names = []

# iterate over the file 
# adding the students name on the list 
with open("namessort.txt") as file: 
    for line in file: 
        names.append(line.rstrip())


# sort the names with sorted
# print the names
for name in sorted(names): 
    print(f"hello, {name}")

