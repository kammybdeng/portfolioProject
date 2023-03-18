import os
from pathlib import Path
import datetime
from pytz import timezone
import pandas as pd

import constant

class fileHandler():

    def __init__(self, filename):
        self.filename = filename
        self.input_path = ''
        self.output_path = ''
        self.ext = ''

    def checkValidInputFile(self):
        self.input_path = Path(constant.FILE_PATH + self.filename)
        return self.input_path.is_file()


    def checkExtension(self):
        # check extension
        if self.filename.endswith('.xlsx'):
            self.ext = '.xlsx'
            return True
        elif self.filename.endswith('.csv'):
            self.ext = '.csv'
            return True
        return False


    def checkValidFile(self):
        if not self.checkValidInputFile():
            print("File not Found. Please place file in 'myFile' folder")
            return False
        else:
            if not self.checkExtension():
                print( 'Not a supported file format')
                return False
        return True
    
    def defaultOutputPath(self):
        self.output_path = constant.FILE_PATH + \
        '_'.join([self.filename.strip(self.ext), 'OUTPUT'] + \
        str(datetime.datetime.now(timezone('US/Pacific')).date()).split('-')) + \
        self.ext


    def read(self):
        stocks = []
        shares = []

        if self.checkValidFile():
            # set default output path after validating the input path
            self.defaultOutputPath()

            if self.ext == '.xlsx':
                df = pd.read_excel(self.input_path)
            else:
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
            





