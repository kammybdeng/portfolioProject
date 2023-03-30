# Portfolio Project 

## Overview
A Python program that takes a spreadsheet with stock tickers and shares to generate a new spreadsheet with latest prices and other information. A tracker that helps organize stocks distributed across different platforms without exposing personal data (since this is a local program without any databases) and get the latest price. A similar replica of the portfolio tracker in [Morning Star](https://www.morningstar.com/).

I'm open to work. Please visit my [LinkedIn](https://www.linkedin.com/in/kammy-deng/) if interested and I'm very happy to receive any feedback on my project.

## Usage
Please name the first two columns as (tickers, shares) and place the spreadsheet inside `myFiles` folder. See examples in `myFiles` folder.


### Get your API key
Please get your free API Keys from [Financial Modeling Prep](https://site.financialmodelingprep.com/developer/docs/) and [Serp API](https://serpapi.com/). Then run the following command to set up the key as your environment variables.

Run command:
```
source setup.sh {Financial Modeling Prep API Key} {Serp API Key}
```

### Run program
Run this program with the command:

```
python3 myPortfolio/stats.py --filename {filename}
```
Please note that to use "filename" instead of the "path", because it assumes you have already put the file inside `myFiles` folder.

## Roadmap / Planning
[Kanban Board](https://www.notion.so/b66f71511b374885bee8aa5e2ddd1566?v=9dc5f1315aaa43a68a3b193c9d5f0d12&pvs=4)

