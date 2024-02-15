def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def len_is_valid(s):
    return 2 <= len(s) <= 6
                           

def starts_with_alpha_is_valid(s):
    return s[0].isalpha() and s[1].isalpha()


def nums_are_valid(s):
    sum = 0 
    digit = False
    
    for c in s[2:]:
        if digit and c.isalpha():
            return False
        
        if c.isdigit():
            sum += int(c)
            
            if sum == 0:
                return False
            
            digit = True
    
    return True       
    
    
def characters_are_valid(s):
    return s.isalnum()


def is_valid(s):
    if not len_is_valid(s):
        return False
    
    if not starts_with_alpha_is_valid(s):
        return False
    
    if not characters_are_valid(s):
        return False
    
    if not nums_are_valid(s):
        return False
    
    return True


if __name__ == '__main__':
    main()