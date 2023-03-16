# Portfolio Project 

## Overview
A Python program that takes a simple spreadsheet with a list of stock tickers and shares, then generates a new spreadsheet with current price and other additional information.

## Motivation
- To build a tracker that helps organize stocks distributed across different platforms without exposing personal data (since this is a local program without any databases) and get the latest price. Personally, I'm trying to build a similar replica of the portfolio tracker in [Morning Star](https://www.morningstar.com/) to organize my own stocks without exposing my own data :)
- To practice OOP principles, proper storage of private keys, usage of logging, etc

## Preque and Usage
Please name your spreadsheet as with two columns (ticker, shares) and place the spreadsheet inside `myFiles` folder. See example in `myFiles` folder.


### Set up your API key
Please set up your API Key at [Financial Modeling Prep](https://site.financialmodelingprep.com/developer/docs/) and set them as your environment variables.

Run command:
```
source setup.sh {Your API Key}
```

### Run program
Run this program with the command:

```
python3 myPortfolio/stats.py --filename {filename}
```


## TODO
### Clean ups
- modify private and public attributes, rename some modules, add argparse to support input params in program
- add requirement.txt or wrap project in docker
- remove the step to setup API key for easier access

### Features
- add NLP model for title sentiment
- add csv file support
- add cryto support 

