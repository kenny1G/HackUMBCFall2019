import json
import requests

class apiParser:
    response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&outputsize=full&symbol=MSFT&apikey=WXCVR1HQHSVB9V2N")
    stocks = json.loads(response.text)

if __name__ == '__main__':
    print(apiParser.stocks["Time Series (Daily)"]["2019-09-27"])
