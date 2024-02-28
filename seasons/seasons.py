from datetime import date, datetime
import sys
import inflect


def main():
    date_input = input("Date of Birth: ")
    date_birth_date = parse_date_birth(date_input) 
    minutes = calcule_minutes(date_birth_date, date.today())
    words = format_response(minutes)
    print(words)


def calcule_minutes(date_birth, today):
    dif = today - date_birth
    return round(dif.total_seconds() / 60)


def format_response(minutes):
    p = inflect.engine()
    words = p.number_to_words(minutes)
    words = words.replace('and ', '').capitalize()
    print(f'{words} minutes')
    

def parse_date_birth(date_birth):
    try:
        return datetime.strptime(date_birth, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please enter a date in the format YYYY-MM-DD.")
        sys.exit(1)


if __name__ == "__main__":
    main()