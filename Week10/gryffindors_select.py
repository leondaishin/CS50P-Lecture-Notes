students = [
    {"name": "hermione", "house": "gryffindor"}, 
    {"name": "harry", "house": "gryffindor"},
    {"name": "ron", "house": "gryffindor"},
    {"name": "draco", "house": "slytherin"},
]


house = input("House: ").lower().strip()

for student in students: 
    if student["house"] == house: 
        print(student["name"])

        