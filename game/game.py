import random 

def main():
    while True:
        try:
            level = input('Level: ')
            num = random.randint(1, int(level))
    
            game(num)
            break
        except (EOFError, ValueError):
            pass

def game(num):
    while True:
        try:
            guess = int(input('Guess: '))
            if guess < 0:
                continue            
            elif guess > num:
                print('Too large!')
                continue         
            elif guess < num:
                print('Too small!')
                continue        
        
            print('Just Right!')
            break
        except EOFError:
            pass
        

if __name__ == '__main__':
    main()