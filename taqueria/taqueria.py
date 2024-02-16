def main():
    dic = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    
    menu(dic)    
    print()
    
def menu(dic):       
    dic_norm = {k.lower(): v for k, v in dic.items()}
    sum = 0    
    
    while True:
        try:
            item = input('Item: ')
            item = item.strip().lower()
        
            if item not in dic_norm:
                continue          
        
            sum += dic_norm[item]
            print(f'${sum:.2f}')
        except EOFError:
            return f'${sum:.2f}'
     

if __name__ == '__main__':
    main()