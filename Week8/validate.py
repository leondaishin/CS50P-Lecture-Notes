# asking email adress and seeing if it is valid or not 

# Input of the emailadress without any spaces ("strip")
email = input("What is yourp email? ").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"): 
    print("Valid")
else: 
    print("Invalid")
