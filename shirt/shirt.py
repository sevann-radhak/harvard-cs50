from PIL import Image, ImageOps
import os, sys

def main():
    check_arg_validity()
    file_check()
    fit_shirt()

def check_arg_validity():
    if len(sys.argv) != 3:
        sys.exit("Invalid command-line arguments.")        
    elif not os.path.isfile(sys.argv[1]):
        sys.exit("Invalid input - Path.")


def file_check():
    formats: list[str] = ["jpg", "jpeg", "png"]
    index_1: any = formats.index(sys.argv[1].split(".")[1])
    index_2: any = formats.index(sys.argv[2].split(".")[1])

    if index_1 is None or index_2 is None:
        sys.exit("Invalid input.")

    if index_2 != index_1:
        sys.exit("Input and output have different extensions.")


def fit_shirt():
    shirt = Image.open("shirt.png")
    image = Image.open(sys.argv[1])

    image = ImageOps.fit(image, shirt.size)
    image.paste(shirt, shirt)
    image.save(sys.argv[2])


if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/shirt
# submit50 cs50/problems/2022/python/shirt