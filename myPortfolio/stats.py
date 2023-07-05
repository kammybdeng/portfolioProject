from fileWizard import fileHandler
from fetcher import StockData
from logger import logger
import formulas

import argparse
import pdb




def main(filename):


    myFile = fileHandler(filename)
    stocks, shares = myFile.read()

    if not stocks or not shares:
        return 'No content in file' 

    tempList = zip(stocks, shares)
    stocksList = []

    
    print('Your list of stocks and shares:\n')
    for i, j in tempList:
        if j < 0:
            print('shares cannot be negative. See log')
            logger.warning(f'Negative share error - Stock: {i} Shares: {j}')
        else:
            stocksList.append((i, j))
            print(i, '\t', j)
    


    outputInfo = []

    for name, shareamt in stocksList:
        data = StockData(name, shareamt)
        
        # profile data
        profileData = data.fetchData('PROFILE')

        # dividend data
        divData = data.fetchData(endpoint='DIVIDEND')

        if not profileData: #(TO-DO) check if can be removed
            continue


        # set current price
        try: #(TO-DO) clean up 
            data.name = profileData[0]['companyName']
            data.price = profileData[0]['price']
            data.sector = profileData[0]['sector'] if profileData[0]['sector'] else 'N/A'
            data.beta = profileData[0]['beta']
            data.EFT = 'Yes' if profileData[0]['isEtf'] else 'No' 
            data.forwardDivAmt = profileData[0]['lastDiv']
        except:
            logger.warning(f'{data.ticker}: profile info setting error')

        # total value
        try:
            data.totalVal = formulas.calTotalVal(data.price, data.shares)
        except:
            logger.warning(f'{data.ticker}: total value error')
            

        # trailing dividend yield
        try:
            data.trailingDiv = formulas.calTrailingDiv(divData['historical'], data.price)
        except:
            logger.warning(f'{data.ticker}: trailing dividend yield error')
            
        try:
            data.getNews()
        except:
            logger.warning(f'{data.ticker}: news fetching error')
        # forward dividend yield
        # try:
        #     data.forwardDiv = formulas.calForwardDiv(data.lastDiv, data.price)
        # except:
        #     logger.warning(f'{data.ticker}: forward dividend yield error')
        #     pass


        infoDict = {}
        for k, v in vars(data).items():
            if '_' not in k:
                infoDict[k] = v
                print(k, v)
        print()
        outputInfo.append(infoDict)

   
    myFile.write(outputInfo)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='myPortfolio',
                    description='Create a real-time file with the selected tickers'
                    )
    parser.add_argument('--filename', type=str, default='portfolio_test.csv')
    args = parser.parse_args()

    main(args.filename)


    