
from urllib.request import urlopen
import certifi
import json
import pdb
import constant



class StockData():

    baseURL = constant.BASEURL
    apiKey = constant.APIKEY

    def __init__(self, name, shares):
        self.name = name
        self.shares = shares
        self.totalVal = 0
        self.price = 0 
        self.trailingDiv = 0 
        self.forwardDivAmt = 0 
        self.beta = 0
        self.industry = ''

        self._profileURL = f"{StockData.baseURL}/api/v3/profile/{self.name}?apikey={StockData.apiKey}"
        self._dividendURL = f"{StockData.baseURL}/api/v3/historical-price-full/stock_dividend/{self.name}?apikey={StockData.apiKey}"
        
    
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
        response = urlopen(url, cafile=certifi.where())
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
        if endpoint=='PROFILE':
            url = self._profileURL
        else:
            url = self._dividendURL

        resp = self.getResponse(url)
        data = self.getJson(resp)
        if saveJson:
            self.saveJson(data, f'./{endpoint}_{self.name}_sample.json')
        return self.getDict(data)

