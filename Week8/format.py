import re

# not starting from 0,1,2... its 1,2,3.. for re library
# format the name not the email adress this time 
name = input("What is your name? ").strip()

matches = re.search(r"^(.+), *(.+)$", name)
if matches: 
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"Hello, {name}")

# if "," in name: 
#    last, first = name.split(", ")
#    name = f"{first} {last}" 
# print(f"Hello, {name}")