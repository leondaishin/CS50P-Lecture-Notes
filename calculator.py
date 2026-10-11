# Ask person for two numbers
#input makes the user type in a number 
#int makes the number an integer not just a string
x = float(input("What is x? "))
y = float(input("What is y? "))

#this rounds the number 
z = round(x / y, 2)

#this prints the number
print(f"{z:.2f}")