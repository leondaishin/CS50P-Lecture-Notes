# file I/O to STORE information 
# to saving the inputs of the names

name = input("What is your name? ")
# open = open a file to put in information to save for 
# open the file names.txt and w for lettzing it change the file to "write" the file
# "a" for append the lists that we are inputting
# here there is appending the names without a space 


#### file = open("names.txt", "a")


# making the names seperated by the space between them by f string with back slash n 


### file.write(f"{name}\n")

# closing the file 
### file.close()



with open("names.txt", "a") as file: 
    file.write(f"{name}\n")




# names list starting from 0 
# names = [] 

# for variable in 0, 1, 2 write names until 3 
# for i in range(3): 
#    names.append(input("What is your name? "))

#for name in sorted(names): 
#    print(f"hello, {name} ")