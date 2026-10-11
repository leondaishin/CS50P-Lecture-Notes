# encapsulate functions in one class (function a , function b)
# organizing the functions and variables that have similarities in a class
# helps organize the code better


# methods are __init__ and __str__: 
class Student: 
    def __init__(self, name, house, patronus):
        # instead of saying if name == "":
        # raising an exception  
        if not name: 
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]: 
            raise ValueError("Invalid House")
        self.name = name 
        self.house = house
        self.patronus = patronus

# __str__(self) always making the strings 
    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus: 
            case "Stag": 
                return "horse emoji"
            case "Otter": 
                return "Otter emoji"
            case "Jack Russell terrier":
                return "dog emoji"
            case _:
                return "nothing"


    # getter for name 
    @property 
    def name(self): 
        return self._name 

    # setter for name 
    @name.setter 
    def name(self, name): 
        if not name: 
            raise ValueError("Missing Name") 
        self._name = name




# getter 
# giving you more controls for the code for the variables stored
    @property
    def house(self): 
        #_ for function not variable
        return self._house

# setter 
    @house.setter
    def house(self, house): 
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House") 
        # _ for function not variable
        self._house = house

# class int(x, base=10)
# int is a class in python

# class str(object='') 
# str is a class
# str.lower() = lowercase 
# str.strip([chars])
# list is a class as well 
# list.append(x)
# class list([iterable])
# dict is a class in python



def main():   
    student = get_student()
    print("Expecto Patronum!") 
    print(student.charm())
    # printing the output of this code
    ### print(f"{student.name} is from {student.house}")
    print(student)


# return student with name and house 
# here we need object oriented programming
def get_student():

    # option 1 to code 
    # constructor call Student(name, house)
    name = input("Name: ") 
    house = input("House: ")
    patronus = input("Patronus: ") 
    return Student(name, house, patronus)

    # option 2 to code
    # variable matches the name of the class 
    # name, house attribute in one (like tupling) 
    
    ### student = Student()
    ### student.name = input("Name: ")
    ### student.house = input("House: ") 
    ### return student



if __name__ == "__main__": 
    main()
