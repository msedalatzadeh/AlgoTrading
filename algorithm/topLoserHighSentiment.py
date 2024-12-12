import sys; sys.path.append('/Users/sajjadedalatzadeh/GitHub/AlgoTrading')
from ai import sentiment
from data import topLosers

def get(numberOfStocks: int) -> str:
    tickers = topLosers.get(numberOfStocks)
    sentiments = {}
    for ticker in tickers:
        sentiments[ticker] = sentiment.getSentiment(ticker)

    maxSentimentTicker = max(sentiments, key=sentiments.get)
    return maxSentimentTicker