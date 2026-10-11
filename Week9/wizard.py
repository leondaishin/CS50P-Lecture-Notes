# inheritance = inherit a subclass in a class
# classes in class (unterklasse oberklasse) 
# the errors are classes (hierarchy of classes with subclasses as well) 
# Class makes the coding make it more organized and beautiful 

class Wizard: 
    def __init__(self, name): 
        if not name: 
            raise ValueError("Missing Name") 
        self.name = name

    ...

# teilmange class wizard in student rein tun 
class Student(Wizard): 
    def __init__(self, name, house):
        # super (obermenge)
        super().__init__(name)

        self.house = house





class Professor(Wizard): 
    def __init__(self, name, subject): 
        super().__init__(name)
        self.subject = subject

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defence Against the Dark Arts")  