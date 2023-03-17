from fileWizard import wizardExcel
from fetcher import StockData
from logger import logger
import constant
import formulas

import argparse
import datetime

import pdb




def main(filename):

    # check extension
    if filename.endswith('.xlsx'):
        ext = '.xlsx'
    elif filename.endswith('.csv'):
        ext = '.csv'
    else:
        print( 'Not a supported file format')
        return 

    inputPath = constant.FILE_PATH + filename
    # (TO-DO) update timezone to PST
    outputPath = constant.FILE_PATH + '_'.join([filename.strip(ext), 'OUTPUT'] + str(datetime.datetime.now().date()).split('-')) + ext

    wEx = wizardExcel(inputPath, outputPath, ext)
    stocks, shares = wEx.read()
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
            data.industry = profileData[0]['industry'] if profileData[0]['industry'] else 'N/A'
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

   
    wEx.write(outputInfo)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='myPortfolio',
                    description='Create a real-time file with the selected tickers'
                    )
    parser.add_argument('--filename', type=str, default='portfolio_test.csv')
    args = parser.parse_args()

    main(args.filename)