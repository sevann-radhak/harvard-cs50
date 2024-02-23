import sys
import os


def count_lines(file):
    count = 0
    try:
        with open(file, 'r') as file:        
            for line in file:
                ls = line.lstrip()
                
                if ls == '\n' or ls == '' or ls.startswith('#'):
                    continue
                
                count += 1
    except FileNotFoundError:
        sys.exit("Invalid file name or file does not exist.")
     
    return count

def main():    
    if len(sys.argv) != 2:
        sys.exit("Invalid command-line arguments.")

    file_name = sys.argv[1]
    if not file_name.endswith('.py'):
        sys.exit("Invalid file name.")

    line_count = count_lines(file_name)
    print(f"{line_count}")


if __name__ == "__main__":
    main()