from collections import Counter

def main():
    r = process()
    
    for k, v in r.items():
        print(f'{v} {k.upper()}')
        

def process():
    list = []
    
    while True:        
        try:
            input_item = input()
            list.append(input_item)
        except EOFError:
            break
    
    list_counter = Counter(list)
    list_counter = dict(sorted(list_counter.items()))   
    
    return list_counter


if __name__ == '__main__':
    main()