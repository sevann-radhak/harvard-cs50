def main():
    camel_case = input('camelCase: ')
    snake_case = convert(camel_case)
    print(snake_case)
    

def convert(s):
    for i in s:
        if i.isupper():
            s = s.replace(i, '_' + i.lower())   
    return s 


if __name__ == '__main__':
    main()