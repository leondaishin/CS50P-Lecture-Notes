def main():

    latitude = input("Enter latitude: ").strip()
    longitude = input("Enter longitude: ").strip()
    

    coordinates = (latitude, longitude)
    print(f"latitude: {coordinates[0]}")
    print(f"longitude: {coordinates[1]}")
    print(f"So the resulting Coordinates are: {coordinates}")


main()