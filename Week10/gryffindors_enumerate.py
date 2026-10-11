# enumerate(iterable, start=0)

students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students): 
    print(i + 1, student)


# other normal way to do this 
### for i in range(len(students)): 
    # i + 1 because Hermione would start with 0
    # python starts with 0 so we need to index verschiebung um 1 
    ### print(i + 1, students[i])