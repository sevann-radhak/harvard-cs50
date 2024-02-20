import sys
from PIL import Image

def main():
    images = []    
    
    for arg in sys.argv[1:]:
        image = Image.open(arg)
        images.append(image)
        
    images[0].save('output.gif', save_all=True, append_images=images[1:], duration=100, loop=0) 

if __name__ == '__main__':
    main()