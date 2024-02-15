import random

coin = random.choice(['heads', 'tails'])

numbers = [1, 2, 3, 4, 5, 6]
random.shuffle(numbers)

for number in numbers:
    print(number)

print('end')