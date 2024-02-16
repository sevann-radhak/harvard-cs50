def main():
    promp = input('Fraction: ')
    frac = convert(promp)
    fr = frac_result(frac)
    
    print(fr)
    
def frac_result(frac):
    if frac <= 1:
        return 'E'
    
    if frac >= 99:
        return 'F'
    
    return f'{frac}%'
    

    

def convert(v):         
    while True:
        f = v.split('/')
        try:
            x = int(f[0])
            y = int(f[1])
            
            if x > y:
                raise ValueError
            
            return round((x/y * 100), 2)
        except (ValueError, ZeroDivisionError, IndexError, TypeError):
            v = input('Fraction: ') 
            pass   


if __name__ == '__main__':
    main()