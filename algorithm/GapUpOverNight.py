from ibapi.client import *
from ibapi.wrapper import *
import sys; sys.path.append('/Users/sajjadedalatzadeh/GitHub/AlgoTrading')
from utility.order import submitOrder
from datetime import datetime
import time

def implement(ticker: str):
  while True:
      now = datetime.now()
      if now.hour==15 and now.minute>=56 and now.minute<=59:
          submitOrder('MKT', 'BUY', ticker)
          break
      if now.hour==4 and now.minute>=5:
          submitOrder('LMT', 'SELL', ticker)
          break
      
      time.sleep(60)