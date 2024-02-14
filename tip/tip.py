def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    try:
        d = d.replace('$', '')
        return float(d)
    except ValueError:
        print(f"Invalid input: {d}. Please enter a valid number.")
        return 0.0


def percent_to_float(p):
    try:
        p = p.replace('%', '')
        return float(p) / 100
    except ValueError:
        print(f"Invalid input: {p}. Please enter a valid number.")
        return 0.0


main()