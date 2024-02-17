import emoji

def main():
    input_text = input('Input: ')
    input_text = input_text.replace('Input: ', '')
    input_text = normalize(input_text)
    input_emojized = emoji.emojize(input_text)
    print(f'Output: {input_emojized}')


def normalize(t):
    t = t.replace(':thumbsup:', ':thumbsup_up:').replace(':earth_asia:', ':globe_showing_Asia-Australia:')
    
    return t

if __name__ == '__main__':
    main()
