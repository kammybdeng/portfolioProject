import openpyxl
import pandas as pd
import pdb

class wizardExcel():

    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def read(self):
        stocks = []
        shares = []

        df = pd.read_excel(self.input_path, sheet_name = 'input_timestamp')
        
        stocks = df['name'].tolist()
        shares = df['shares'].tolist()
                
        return stocks, shares

    def build(self, listOfDict):
        return pd.DataFrame.from_records(listOfDict, index=[i for i in range(len(listOfDict))])

    def write(self, listOfDict):
        df = self.build(listOfDict)
        df.to_excel(excel_writer = self.output_path, index=False)
            





