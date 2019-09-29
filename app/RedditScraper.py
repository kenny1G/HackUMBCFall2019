import praw
import json
import requests
import datetime as dt
from datetime import datetime
class RedditScraper:
    alphaResponse = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&outputsize=full&symbol=MSFT&apikey=WXCVR1HQHSVB9V2N")
    stocks = json.loads(alphaResponse.text)
    reddit = praw.Reddit(client_id = 'Adp2y8pmTrKfoQ', client_secret = 'nckgI9sZhQzo0UnPBcL5j5NwLnk', user_agent='WallStreetBetsBets')
    subreddit = reddit.subreddit('wallstreetbets')
    top_subreddit = subreddit.search("facebook")
    topics_dict = {"title":[],"score":[],"created":[]}

    def utf_to_string(utf):
        return datetime.utcfromtimestamp(int(utf)).strftime('%Y-%m-%d')

    for submission in top_subreddit:
        topics_dict["title"].append(submission.title)
        topics_dict["score"].append(submission.score)
        topics_dict["created"].append(utf_to_string(submission.created))

    # for date in top_subreddit["created"]:
    #     #print(stocks["Time Series (Daily)"][date])


if __name__ == '__main__':
    for date in RedditScraper.topics_dict["created"]:
        if date in RedditScraper.stocks["Time Series (Daily)"]:
            print(date)
            print(RedditScraper.stocks["Time Series (Daily)"][date])
