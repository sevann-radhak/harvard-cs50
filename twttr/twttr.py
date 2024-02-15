def main():
    tweet = input('Input: ')
    twt = convert(tweet)
    print(twt)
    

def convert(s):      
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels.extend([v.upper() for v in vowels])
    
    for v in vowels:
        s = s.replace(v, '')
        
    return s


if __name__ == '__main__':
    main()