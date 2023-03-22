from serpapi import GoogleSearch
from constant import SEARCH_API_KEY
import pdb

class NewsSearch():


    def __init__(self, ticker):
        self.ticker = ticker
        self.topk = 5

    def search(self):
        params = {
        "q": self.ticker + ' stock news today',
        "tbm": "nws",
        "location": "California",
        "api_key": SEARCH_API_KEY
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        news_results = results["news_results"]
        return news_results


    def getTopkNews(self):
        
        news = self.search()
        selected_news = news[:self.topk]
        headlines = [i['title'] for i in selected_news]
        return headlines

if __name__ == "__main__":
    ele = NewsSearch('AAPL')
    headlines = ele.getTopkNews()
    print(headlines)