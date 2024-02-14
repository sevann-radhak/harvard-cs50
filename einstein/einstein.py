def main():
    input_string = input('Type m: ')
    
    try:
        m = int(input_string)
        c = 300000000
        e = m * (c ** 2)
        print(e)
    except ValueError:
        print(f'Invalid input: {input_string}. Please enter a valid number.')
        return
    

if __name__ == '__main__':
    main()
