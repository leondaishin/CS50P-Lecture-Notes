students = [
    {"name": "Hermione", "house": "Gryffindor"}, 
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]


# the list of students who live in gryffindor
gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors): 
    print(gryffindor)

# the list of students who live in Slytherin
slytherins = [
    student["name"] for student in students if student["house"] == "Slytherin"
]

for slytherin in sorted(slytherins): 
    print(slytherin)