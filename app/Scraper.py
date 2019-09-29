import praw
import json
import requests
import datetime as dt
from datetime import datetime
class Scraper:

    def __init__(self,query):
        self.query = query
        alphaResponse = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&outputsize=full&symbol=MSFT&apikey=WXCVR1HQHSVB9V2N")
        self.stocks = json.loads(alphaResponse.text)
        self.reddit = praw.Reddit(client_id = 'Adp2y8pmTrKfoQ', client_secret = 'nckgI9sZhQzo0UnPBcL5j5NwLnk', user_agent='WallStreetBetsBets')
        self.subreddit = self.reddit.subreddit('wallstreetbets')
        self.top_subreddit = self.subreddit.search(self.query)
        self.topics_dict = {"title":[],"score":[],"created":[]}
        self.make_reddit_dict()

    def utf_to_string(self,utf):
        return datetime.utcfromtimestamp(int(utf)).strftime('%Y-%m-%d')

    def make_reddit_dict(self):
        for submission in self.top_subreddit:
            self.topics_dict["title"].append(submission.title)
            self.topics_dict["score"].append(submission.score)
            self.topics_dict["created"].append(self.utf_to_string(submission.created))

    def get_reddit_titles(self):
        return self.topics_dict["title"]

    def get_reddit_scores(self):
        return self.topics_dict["score"]

    def get_reddit_dates(self):
        return self.topics_dict["created"]

    def get_stocks(self,date):
        if date in self.stocks["Time Series (Daily)"]:
            return self.stocks["Time Series (Daily)"][date]
