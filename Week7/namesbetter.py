# r for reading the file 
with open("namesbetter.txt", "r") as file:
    # reading the lines of the file
    # making it into the variable file.readlines 
    lines = file.readlines()

for line in lines: 
    print("hello,", line)


