students = [
    {"name": "Hermione", "house": "Gryffindor"}, 
    {"name": "Harry", "house": "Gryffindor"}, 
    {"name": "Ron", "house": "Gryffindor"}, 
    {"name": "Draco", "house": "Slytherin"}, 
    {"name": "Padma", "house": "Ravenclaw"}, 
]

# not [] but set()
# no duplicates can exist
houses = set()
for student in students: 
    # not append() but here because of set() we have add() 
    houses.add(student["house"])


    for house in sorted(houses):
        print(house)