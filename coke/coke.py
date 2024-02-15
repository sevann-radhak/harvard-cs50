from decimal import Decimal

def main():
    amount_due = 50
    accepted_coins = [5, 10, 25]
    change = insert_coins(amount_due, accepted_coins)
    print(f'Change Owed: {change}')


def insert_coins(amount_due, accepted_coins):
    amount = 0

    while amount < amount_due:
        print(f'Amount Due: {amount_due - amount}')
        inserted_coin = int(input('Insert coin: '))

        if inserted_coin not in accepted_coins:
            print('Please insert a valid coin.')
            continue

        amount += inserted_coin

    return amount - amount_due


if __name__ == '__main__':
    main()
