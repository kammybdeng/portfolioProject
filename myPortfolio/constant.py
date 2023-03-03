import os

API_KEY = os.environ["API_KEY"]
BASE_URL = os.environ['BASE_URL']
INPUT_PATH = './myFiles/portfolio_test.xlsx'
OUTPUT_PATH = './myFiles/portfolio_test_output.xlsx'


# fileWizard
INPUT_SHEETNAME = 'input_timestamp'
INPUT_TICKER_COLM = 'ticker'
INPUT_SHARES_COLM = 'shares' 