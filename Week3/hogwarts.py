# list of students and houses 
#associating student with each house
students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

#range is only for integers but students is a list 
#we do len(studnets) to make it into an integer
for i in range(len(students)): 
    print(i + 1, students[i])

# u can write for i in students: print(i) but student is better to understand
#for student in students: 
#    print(student)


#how to iterate whe nth word of the list i had so for 0 its erminione 1 its harry and 2 its ron##
#print(students[0])
