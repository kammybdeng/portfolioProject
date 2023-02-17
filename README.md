# Portfolio Project 

## Overview
A Python program that takes a simple excel file with a list of stock names and shares, then generates a new excel file with current price and other additional information.

## Motivation
- To build a tracker that helps organize stocks distributed across different platforms without exposing personal data (since this is a local program without any databases) and get the latest price. Personally, I'm trying to build a similar replica of the portfolio tracker in [Morning Star](https://www.morningstar.com/) to organize my own stocks without exposing my own data :)
- To practice OOP principles, proper storage of private keys, usage of logging, etc

## Preque and Usage
Please name your excel sheet as `input_timestamp` with two columns (name, shares) and place the excel file inside this folder. See example below 

| name  | shares |
| ----- | ----- |
| AAPL  | 20  |
| TSLA  | 10  |
| VOO  | 30  |

### Set up your API key
Please set up your API Key at [Financial Modeling Prep](https://site.financialmodelingprep.com/developer/docs/) and set them as your environment variables.

Run command:
```
export FMPAPIKey={Your API Key}
export FMPBaseURL='https://financialmodelingprep.com'
```

### Run program
Finally you can run this program with the command:

```
python3 stats.py
```


## TODO
### Clean ups
- modify private and public attributes, rename some modules, add argparse to support input params in program
- add requirement.txt or wrap project in docker
- remove the step to setup API key for easier access

### Features
- add csv file support
- add sample ML models for prediction
- add cryto support 

