def main():
    user_input = input("Please enter a sentence: ")
    text = convert(user_input)
    print(text)


def convert(s):
    return s.replace(':)', '🙂').replace(':(', '🙁')


if __name__ == "__main__":
    main()
