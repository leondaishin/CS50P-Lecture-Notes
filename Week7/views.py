import numpy as np
from PIL import Image

def main(): 
    with open("views.csv", "r") as file: 
        reader = csv.DictReader(file)
        for row in reader:
            brightness = calculate_brightness("{row['id]}")
            print(row["id"])


def calculate_brightness(filenames): 
    with Image.open(filename) as 
        brightness == np.mean(np.array(image.convert("L"))) / 255
    return brightness 
