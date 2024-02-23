from validator_collection import validators, checkers, errors

def main():
    email = input("What's your email address?: ")
    is_valid = validate_checkers(email)
    
    print(f'Valid' if is_valid else f'Invalid')
    

def validate_checkers(e):
        return checkers.is_email(e)
    

def validate_validators(e):
    try:
        validators.email(e)
        return True
    except errors.NotAnEmail:
        return False
    
if __name__ == "__main__":
    main()