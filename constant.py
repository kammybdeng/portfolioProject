import os

APIKEY = os.environ["FMPAPIKey"]
BASEURL = os.environ['FMPBaseURL']
INPUT_PATH = 'portfolio_test.xlsx'
OUTPUT_PATH = 'portfolio_test_output.xlsx'


# fileWizard
INPUT_SHEETNAME = 'input_timestamp'
INPUT_TICKER_COLM = 'ticker'
INPUT_SHARES_COLM = 'shares' 