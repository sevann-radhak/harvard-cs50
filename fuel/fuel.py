# # def main():
# #     promp = input('Fraction: ')
# #     frac = convert(promp)
# #     fr = frac_result(frac)
    
# #     print(fr)
    
    
# # def frac_result(frac):
# #     if frac <= 1:
# #         return 'E'
    
# #     if frac >= 99:
# #         return 'F'
    
# #     return f'{frac}%'
    
    
# # def convert(v):         
# #     while True:
# #         f = v.split('/')
# #         try:
# #             x = int(f[0])
# #             y = int(f[1])
            
# #             if x > y:
# #                 raise ValueError
            
# #             return round((x/y * 100), 2)
# #         except (ValueError, ZeroDivisionError, IndexError, TypeError):
# #             v = input('Fraction: ') 
# #             pass   


# # if __name__ == '__main__':
# #     main()
        
    
# def main():
#     fraction = input('Fraction: ')
#     perc = convert(fraction)
#     print(gauge(perc))


# def convert(fraction):
#     f = fraction.split('/')    
#     x = f[0]
#     y = f[1]
    
#     if not x.isdigit() or not y.isdigit():
#         raise ValueError
#     if x > y:
#         raise ValueError
#     if y == 0:
#         raise ZeroDivisionError
        
#     x = int(x)
#     y = int(y)
    
#     return round((x/y * 100), 2)


# def gauge(percentage):
#     if percentage <= 1:
#         return 'E'
    
#     if percentage >= 99:
#         return 'F'
    
#     return f'{percentage}%'


# if __name__ == "__main__":
#     main()


def main():
    num = input("Fraction: ")
    percentage = convert(num)
    print(gauge(percentage))


def convert(num):
    while True:
        index = num.find("/")
        try:
            x = int(num[:index])
            y = int(num[index+1:])
            fraction = x / y
            if x > y:
                num = input("Fraction: ")
                continue

            else:
                percentage = int(fraction * 100)
                return percentage

        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage >= 99:
        return "F"

    elif percentage <= 1:
        return "E"

    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()