def main():
    expression = input('Expression: ')
    print(calculate(expression))

def calculate(expression):
    x, y, z = expression.split()
    
    if y == '/' and z == '0':
        return 'Error: Division by zero'
    
    return float(eval(f'{x} {y} {z}'))    


if __name__ == '__main__':
    main()