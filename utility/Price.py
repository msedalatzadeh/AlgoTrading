from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import threading
import time
from datetime import datetime
from ibapi.ticktype import TickTypeEnum

class priceApi(EWrapper, EClient):
	def __init__(self):
		EClient.__init__(self, self)
		self.stockPrice = None
	
	def tickPrice(self, reqId, tickType, price, attrib):
		now = datetime.now()
		isMarketClosed = now.hour>=16 or now.hour< 9 or (now.hour==9 and now.minute<30)
		#print(tickType, price)
		if not self.stockPrice and tickType == 4  and reqId == 1:
			self.stockPrice = price
		elif not self.stockPrice and tickType == 68 and reqId == 1:
			self.stockPrice = price
		elif not self.stockPrice and isMarketClosed and tickType == 75 and reqId == 1:
			self.stockPrice = price
			

def getStockPrice(ticker: str) -> float:
	app = priceApi()
	app.connect('127.0.0.1', 7497, 123)

	#Start the socket in a thread
	api_thread = threading.Thread(target=app.run, daemon=True)
	api_thread.start()

	time.sleep(1) #Sleep interval to allow time for connection to server
	app.reqMarketDataType(3)

	#Create contract object
	contract = Contract()
	contract.symbol = ticker
	contract.secType = 'STK'
	contract.exchange = 'SMART'
	contract.currency = 'USD'

	#Request Market Data
	app.reqMktData(1, contract, '', False, False, [])

	time.sleep(10) #Sleep interval to allow time for incoming price data
	app.disconnect()

	return float(app.stockPrice) if app.stockPrice is not None else None