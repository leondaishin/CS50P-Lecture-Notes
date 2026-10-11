import re

locations = {"+1": "United States and Canada", "+62": "Indonesia", "+505": "Nicaragua"}

def main(): 
    # () = capture group 
    # to name a capture group (?<name of capture group>...)
    pattern = r"?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    number = input("Number: ")

    match = re.research(pattern, number)
    if match: 
        country_code = match.group(country_code)
        print(locations[country_code])
        print("Valid")
    else: 
        print("Invalid")

        
