from fileWizard import wizardExcel
from fetcher import StockData
from logger import logger
import constant
import formulas
import pdb

def main():

    wEx = wizardExcel(constant.INPUT_PATH, constant.OUTPUT_PATH)
    stocks, shares = wEx.read()


    print('Your list of stocks and shares:\n')
    for i, j in zip(stocks, shares):
        print(i, '\t', j)
    stocksList = zip(stocks, shares)


    outputInfo = []

    for name, shareamt in stocksList:
        data = StockData(name, shareamt)
        
        # profile data
        profileData = data.fetchData(endpoint='PROFILE', saveJson=True)

        # dividend data
        divData = data.fetchData(endpoint='DIVIDEND')


        # set current price
        try:
            data.price = profileData[0]['price']
            data.industry = profileData[0]['industry']
            data.beta = profileData[0]['beta']
            data.forwardDivAmt = profileData[0]['lastDiv']
        except:
            logger.warning(f'{data.name}: profile info setting error')

        # total value
        try:
            data.totalVal = formulas.calTotalVal(data.price, data.shares)
        except:
            logger.warning(f'{data.name}: total value error')
            pass

        # trailing dividend yield
        try:
            data.trailingDiv = formulas.calTrailingDiv(divData['historical'], data.price)
        except:
            logger.warning(f'{data.name}: trailing dividend yield error')
            pass

        # forward dividend yield
        # try:
        #     data.forwardDiv = formulas.calForwardDiv(data.lastDiv, data.price)
        # except:
        #     logger.warning(f'{data.name}: forward dividend yield error')
        #     pass


        infoDict = {}
        for k, v in vars(data).items():
            if '_' not in k:
                infoDict[k] = v
                print(k, v)
        print()
        outputInfo.append(infoDict)

        #print(pdb.set_trace())
   
    wEx.write(outputInfo)


if __name__ == "__main__":
    main()