
from urllib.request import urlopen
import certifi
import json
import pdb
import constant
from logger import logger



class StockData():

    baseURL = constant.BASE_URL
    apiKey = constant.API_KEY

    def __init__(self, ticker, shares):
        self.ticker = ticker
        self.name = ''
        self.shares = shares
        self.totalVal = 0
        self.price = 0 
        self.trailingDiv = 0 
        self.forwardDivAmt = 0 
        self.beta = 0
        self.EFT = 'N/A'
        self.industry = 'N/A'

        self._profileURL = f"{StockData.baseURL}/api/v3/profile/{self.ticker}?apikey={StockData.apiKey}"
        self._dividendURL = f"{StockData.baseURL}/api/v3/historical-price-full/stock_dividend/{self.ticker}?apikey={StockData.apiKey}"
        
    
    # @property
    # def trailingDiv(self):
    #     return self._trailingDiv


    # @trailingDiv.setter
    # def trailingDiv(self, value):
    #     if value < 0:
    #         raise ValueError("Div yield should not be negative")
    #     self._trailingDiv = value

    # def setPrice(self, price):
    #     self.price = price

    def getResponse(self, url):
        response = None
        try:
            response = urlopen(url, cafile=certifi.where())
        except:
            logger.debug('Request failed')
        return response
    
    def getJson(self, response):
        return response.read().decode("utf-8")
        
    
    def getDict(self, data):
        return json.loads(data)

    def saveJson(self, data, path):
        with open(path, 'w') as f:
            f.write(data)


    def fetchData(self, endpoint='PROFILE', saveJson=False):
        url = ''
        data = {}

        if endpoint=='PROFILE':
            url = self._profileURL
        else:
            url = self._dividendURL

        resp = self.getResponse(url)
        if resp:
            data = self.getJson(resp)
            if data == '[]':
                logger.warning(f'Request response is empty: {self.ticker}')
            if saveJson:
                self.saveJson(data, f'./{endpoint}_{self.ticker}_sample.json')
            return self.getDict(data)
        else:
            return data

