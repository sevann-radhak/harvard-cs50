import csv
import sys
from tabulate import tabulate


def format(file):
    try:
        with open(file, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            # content = 
            # print(f'Headers: {headers}')
            # print(f'Content: {content}')
            data = [row for row in reader]
            return tabulate(data, headers=headers, tablefmt="grid")
    except FileNotFoundError:
        sys.exit("Invalid file name or file does not exist.")
     

def main():
    if len(sys.argv) != 2:
        sys.exit("Invalid command-line arguments.")

    file_name = sys.argv[1]
    if not file_name.endswith('.csv'):
        sys.exit("Invalid file name.")

    formated = format(file_name)
    print(f"{formated}")

if __name__ == "__main__":
    main()