# name = input('What is your name? ')

# with open('names.txt', 'a') as file:
#     file.write(f'{name}\n') 

students = []

with open('names.csv', 'r') as file:
    # names = sorted(file.readlines(), key=, reverse=True)
    for line in file:
        row = line.strip().split(',')
        student = {'name': row[0], 'age': row[1], 'city': row[2]}
        students.append(student)

for student in sorted(students, key=lambda student: student['name']):
    print(student)


# for name in sorted(names):
#     print(name.strip())

# file = open('names.txt', 'a')
# file.write(f'{name}\n')
# file.close()