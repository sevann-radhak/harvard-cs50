# import csv
# import sys


# def format(file_name_before, file_after):
#     try:
#         with open(file_name_before, 'r') as file_name_before:
#             reader = csv.reader(file_name_before)
#             name_header, house_header = next(reader)
#             data = [row for row in reader]  # Store the rest of the rows in data
#             new_data = []
            
#             for d in data:
#                 last_name, first_name = d[0].split(', ')
#                 name = f"{first_name} {last_name}"
#                 house = d[1]                
#                 new_data.append([name, house])
                
#             print(f'new_data: {new_data}')
            
            
#             with open(file_after, 'w', newline='') as file:
#                 writer = csv.writer(file)
#                 writer.writerows(new_data)
#     except FileNotFoundError:
#         sys.exit("Invalid file name or file does not exist.")
     

# def main():
#     if len(sys.argv) != 3:
#         sys.exit("Invalid command-line arguments.")

#     file_name_before = sys.argv[1]
#     file_name_after = sys.argv[2]
#     if not file_name_before.endswith('.csv') or not file_name_after.endswith('.csv'):
#         sys.exit("Invalid file name.")

#     # file_name = "before.csv"
#     formated = format(file_name_before, file_name_after)
#     print(f"{formated}")


# if __name__ == "__main__":
#     main()





import sys, csv


def main():
    check_arg_validity()
    scourgify()


def check_arg_validity():
    if len(sys.argv) != 3:
        sys.exit("Invalid command-line arguments.")
    
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file.")


def scourgify():
    try:
        input_file = open(sys.argv[1], "r")
        output_file = open(sys.argv[2], "w")
    
    except FileNotFoundError:
        sys.exit("Could not read file")
    
    column_data = csv.DictReader(input_file, delimiter=",")
    column_writer = csv.DictWriter(output_file, ["first", "last", "house"])

    column_writer.writeheader()

    for row in column_data:
        last, first = row["name"].split(",")
        column_writer.writerow({
            "first": first.strip(), 
            "last": last, 
            "house": row["house"]
        })

if __name__ == "__main__":
    main()
    
# check50 cs50/problems/2022/python/scourgify
# submit50 cs50/problems/2022/python/scourgify