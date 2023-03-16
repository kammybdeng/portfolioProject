import pandas as pd
import constant

class wizardExcel():

    def __init__(self, input_path, output_path, ext):
        self.input_path = input_path
        self.output_path = output_path
        self.ext = ext

    def read(self):
        stocks = []
        shares = []

        if self.ext == '.xlsx':
            df = pd.read_excel(self.input_path)
        elif self.ext == '.csv':
            df = pd.read_csv(self.input_path)
        
        stocks = df[constant.INPUT_TICKER_COLM].tolist()
        shares = df[constant.INPUT_SHARES_COLM].tolist()
                
        return stocks, shares

    def build(self, listOfDict):
        return pd.DataFrame.from_records(listOfDict)

    def write(self, listOfDict):
        
        df = self.build(listOfDict)

        if self.ext == '.xlsx':
            df.to_excel(excel_writer = self.output_path, index=False)
        elif self.ext == '.csv':
            df.to_csv(self.output_path, index=False)
            





