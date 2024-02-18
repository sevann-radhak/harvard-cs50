import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit('Missing command-line argument')
    else:
        try:
            b = float(sys.argv[1])
            process(b)
        except ValueError:
            sys.exit('Command-line argument is not a number')            
    

def process(b):
    try:
        req =  requests.get('https://api.coindesk.com/v1/bpi/currentprice.json') 
        bitcoin_usd = req.json()['bpi']['USD']['rate_float']    
        total = bitcoin_usd * b
        print(f"${total:,.4f}")
    except (requests.exceptions.RequestException, requests.RequestException) as e:
        print('Error:', e)
        sys.exit(1)

if __name__ == '__main__':
    main()