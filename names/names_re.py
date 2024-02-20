import re

def main():    
    email = "sevann_2@harvard.EDU"
    if re.search(r"^[^\d\s]\w+@(\w+\.)?\w+\.(edu|gov|org)$", email, re.IGNORECASE):
        print('Email is valid')
    else:
        print('Email is NOT valid')


if __name__ == '__main__':
    main()