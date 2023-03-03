import openpyxl
import pandas as pd
import constant

class wizardExcel():

    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def read(self):
        stocks = []
        shares = []

        df = pd.read_excel(self.input_path, sheet_name = constant.INPUT_SHEETNAME)
        
        stocks = df[constant.INPUT_TICKER_COLM].tolist()
        shares = df[constant.INPUT_SHARES_COLM].tolist()
                
        return stocks, shares

    def build(self, listOfDict):
        return pd.DataFrame.from_records(listOfDict, index=[i for i in range(len(listOfDict))])

    def write(self, listOfDict):
        df = self.build(listOfDict)
        df.to_excel(excel_writer = self.output_path, index=False)
            





