def area(length, width):
    return length * width


def main():
    x = float(input("What is the length of the room? "))
    y = float(input("What is the width of the room? "))
    z = float(input("What is the length of the yard? "))
    w = float(input("What is the width of the yard? "))

    house = area(x, y)
    yard = area(z, w)
    total = house + yard

    print(f"The area of the room is {house} square meters")
    print(f"The area of the yard is {yard} square meters")
    print(f"The total area of the house and yard is {total} square meters")


if __name__ == "__main__":
    main()
