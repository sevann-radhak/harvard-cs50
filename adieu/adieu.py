import inflect

p = inflect.engine()

def adieu():
    names = []
    while True:
        try:
            input_text = input("Name: ")
            names.append(input_text)
        except (KeyboardInterrupt, EOFError):
            break

    text = p.join(names)

    print(f'Adieu, adieu, to {text}')


if  __name__ == '__main__':
    from adieu import adieu
    adieu()
