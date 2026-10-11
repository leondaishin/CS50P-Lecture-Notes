def main():   
    student = get_student()

    if student["name"] == "Padma": 
        student["house"] = "Ravenclaw"
    
    # printing the output of this code
    print(f"{student['name']} is from {student['house']}")

# return student with name and house 
# here we need object oriented programming
def get_student(): 
    student = {}
    student["name"] = input("Name: ") 
    student["house"] = input("House: ") 

    # return multiple values with a comma (works for python only)
    # name, house == tuple which is ONE VALUE tupled with a ","
    # tuple student[0] = name and student[1] = house 
    ### return [name, house]

    return student



if __name__ == "__main__": 
    main()
