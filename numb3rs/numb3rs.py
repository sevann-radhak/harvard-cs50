import re
import sys


def main():
    ipv4 = input("IPv4 Address: ")
    print(validate(ipv4))


def validate(ip):    
    regex = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])$'

    matches = re.search(regex, ip)
    if matches:
        return True
    return False


if __name__ == "__main__":
    main()