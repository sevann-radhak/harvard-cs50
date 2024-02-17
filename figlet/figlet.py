import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

def main():
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        f = random.choice(fonts)
        figlet.setFont(font=f)
    elif len(sys.argv) == 3:
        arg = sys.argv[1]
        v = sys.argv[2]
        if arg_is_valid(arg) and font_is_valid(v):
            figlet.setFont(font=v)
        else:
            sys.exit('Error: Invalid argument or font.')    
    else:
        sys.exit('Error: Invalid amount of arguments.')

    text = input('Input: ')
    print(figlet.renderText(text))
    
    
def font_is_valid(f):
    if f in figlet.getFonts():
        return True


def arg_is_valid(a):
    if a == '-f' or a == '--font':
        return True
    return False


if __name__ == '__main__':
    main()
