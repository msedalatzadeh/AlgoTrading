from ibapi.client import *
from ibapi.wrapper import *
import sys; sys.path.append('/Users/sajjadedalatzadeh/GitHub/AlgoTrading')
from utility import order, price
from algorithm import topLoserHighSentiment
from datetime import datetime
import time

def implement(ticker: str = None):
  purchased = False
  while True:
      now = datetime.now()
      if purchased:
        currentPrice = price.getStockPrice(ticker)
        twoPercentUp = ((currentPrice - avgFillPrice) / avgFillPrice * 100 >= 2)
      if not purchased and now.hour==15 and now.minute>=56 and now.minute<=59:
        if not ticker:
            ticker = topLoserHighSentiment.get(10)
        avgFillPrice = order.submitOrder('MKT', 'BUY', ticker, 10)
        purchased = True
        break
      if purchased and (twoPercentUp or now.hour==4 and now.minute>=5):
        order.submitOrder('LMT', 'SELL', ticker, 10)
        purchased = False
        ticker = None
        break
      
      time.sleep(60)