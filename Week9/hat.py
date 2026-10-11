import random

# sorting the hat to the house the student should be at 
class Hat:

    # storing the list of legal houses 
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name): 
        print(name, "is in", random.choice(cls.houses)) 


Hat.sort("Harry") 