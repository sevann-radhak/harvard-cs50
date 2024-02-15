def main():
    fruit = input('Item: ')
    calories(fruit)
    

def calories(f):      
    calories = {
        'Apple': 130, 
        'Avocado': 50, 
        'Banana': 110, 
        'Cantaloupe': 50,
        'Grapefruit': 60,
        'Grapes': 90,
        'Honeydew': 50,
        'Kiwifruit': 90,
        'Lemon': 15,
        'Lime': 20,
        'Nectarine': 60,
        'Orange': 80,
        'Peach': 60,
        'Pear': 100,
        'Pineapple': 50,
        'Plums': 70,
        'Strawberries': 50,
        'Sweet Cherries': 100,
        'Tangerine': 50,
        'Watermelon': 80
        }
    
    calories_normalized = {k.lower(): v for k, v in calories.items()}
    
    c = calories_normalized.get(f.lower())
    
    if c:
        print(c)

if __name__ == '__main__':
    main()