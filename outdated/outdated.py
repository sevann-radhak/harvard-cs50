def main():
    r = process()
    print(f'{r}')


def process():
    M = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        try:
            input_date = input('Date: ')
            input_date = input_date.strip()
            input_date_parts_1 = input_date.split(' ')
            input_date_parts_2 = input_date.split('/')
            month_number = 0
            
            if len(input_date_parts_1) == 3:
                month = input_date_parts_1[0]
                day = input_date_parts_1[1]
                year = int(input_date_parts_1[2])
                
                if month not in M:
                    continue
                if not day.endswith(','):
                    continue
                
                day = day[:-1]
                day = int(day)   
                
                month_number = M.index(month) + 1            
            elif len(input_date_parts_2) == 3:                
                month_number = int(input_date_parts_2[0])
                day = int(input_date_parts_2[1])
                year = int(input_date_parts_2[2])
            else:
                continue
            
            if day > 31 or month_number < 1 or month_number > 12 or year < 0:
                continue
            
            return f'{year:04}-{month_number:02}-{day:02}'
        except (EOFError, ValueError, IndexError, TypeError, AttributeError, NameError):
            continue


if __name__ == '__main__':
    main()
