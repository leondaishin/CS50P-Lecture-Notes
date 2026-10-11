import sys
import requests

# recall if u input on the command line ->
# it is sys.argv[n] so sys.argv[0] would be "bitcoin.py"

def main():
    # check command-line argument
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")


    # looking if there is exactly one argument
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")


    # request bitcoin price
    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=e1332f9ecae80d68412f64556061a61e891b4aed20def19fb78b4da333120d8c"
            )

    except requests.RequestException as e:
        # exit here
        sys.exit("Request failed")

    # extract json file
    data = response.json()


    # extracting bitcoin price
    price = float(data["data"]["priceUsd"])



    # calculating it into US Dollars:
    bitcoin_amount = bitcoins * price


    # printing the bitcoin price in US Dollars
    print(f"${bitcoin_amount:,.4f}")


if __name__ == "__main__":
    main()