import requests

def get_random_quote():
    url = "https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        quote_data = response.json()
        quote = quote_data['quoteText']
    
    return quote.strip(" ")

if __name__ == '__main__':
    print(get_random_quote())