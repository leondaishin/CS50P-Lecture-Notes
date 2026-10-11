def main():
    number = input("Enter a phone number: ").strip()
    phone = input("Enter 'first' to get the country code or 'last' to get the last 4 digits: ").strip()
    if phone == "first": 
        print(number[0:3]) # gives the country code
    elif phone == "last": 
        print(number[-4:]) # gives the last 4 digits of the phone number)
    else: 
        print(number)


main()