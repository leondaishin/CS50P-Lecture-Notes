students = []

with open("students.csv") as file: 
    for line in file: 
        # split the word with comma of the csv (for google sheet or excel stuff)
        row = line.rstrip().split(",")
        students.append(f"{row[0]} is in {row[1]}")
        # row[0] is the names spalte 
        # row[1] is the house spalte 
        ### print(f"{row[0]} is in {row[1]}")


for student in sorted(students): 
    print(student)




# or u can also say row = name, house and 
# row[0] = name 
# row[1] = house 
# but i prefer this cryptic because the list can be longer. 
