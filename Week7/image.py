from PIL import Image 
from PIL import ImageFilter

def main(): 
    with Image.open("math.png") as img:
        img = img.filter(ImageFilter.FIND_EDGES)
        print(img.size)
        print(img.format)
        img.save("mathedges.png")


main()