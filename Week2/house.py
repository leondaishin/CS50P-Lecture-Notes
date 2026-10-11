name = input("What is your name? ")

match name: 
    case "Harry": 
        print("Gryffindor")
    case "Hermione": 
        print("Gryffindor")
    case "Ron": 
        print("Gryffindor")
    case "Draco": 
        print("Slytherin")
    case _:
        print("This person is undefined.")


#Doing it with ifs: 

#if name == "Harry": 
#    print("Gryffindor")
#elif name == "Draco":
#    print("Slytherin")
#elif name == "Luna":
#    print("Ravenclaw")
#elif name == "Cedric":
#    print("Hufflepuff")
#elif name == "Hermione":
#    print("Gryffindor")
#else: 
#    print("You are not in Hogwarts")

