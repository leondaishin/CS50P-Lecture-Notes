#How to associate each student to house inefficiently 
#students = {"Hermione": "Gryffindor", "Harry": "Gryffindor", ...}

#Dictionary defining each colomn: 
students = [
    {"name": "Hermione", "house":"Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students: 
    print(student["name"], "lives in", student["house"], "and has the superpower", student["patronus"])


# better way to write it down: 
#students = {
#    "Hermione": "Gryffindor",
#    "Harry": "Gryffindor",
#    "Ron": "Gryffindor",
#    "Draco": "Slytherin",
#}

#printing the students and the houses defined by the Dictionary
#for student in students: 
#    print(student, "lives in ", students[student])


# how to manually do it, so associating the student with the house
#print(students["Hermione"])
#print(students["Harry"])
#print(students["Ron"])
#print(students["Draco"])
