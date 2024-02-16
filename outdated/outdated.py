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
            parts = input_date.strip().split(' ')

            if len(parts) != 3:
                parts = input_date.split('/')
                if(len(parts) != 3):
                    continue

            day = int(parts[1])
            month = parts[0]
            year = int(parts[2])

            if day > 31:
                continue

            if year < 0:
                continue

            month_number = 0

            if month in M:
                month_number = M.index(month) + 1
            elif month.isnumeric():
                month_number = int(month)

                if month_number < 1 or month_number > 12:
                    continue
            else:
                continue

            return f'{year:04}-{month_number:02}-{day:02}'
        except (EOFError, ValueError, IndexError, TypeError, AttributeError, NameError):
            break

    return


if __name__ == '__main__':
    main()
