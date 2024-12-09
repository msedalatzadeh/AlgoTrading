from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from threading import Timer

class AccountApi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.balanceInCAD = 0
        self.balanceInUSD = 0

    #def error(self, reqId, errorCode, errorString, advancedOrderReject=""):
    #    print("Error: ", reqId, " ", errorCode, " ", errorString)

    def nextValidId(self, orderId):
        self.start()

    #def updatePortfolio(self, contract: Contract, position: float, marketPrice: float, marketValue: float,
    #                    averageCost: float, unrealizedPNL: float, realizedPNL: float, accountName: str):
        #print("UpdatePortfolio.", "Symbol:", contract.symbol, "SecType:", contract.secType, "Exchange:", contract.exchange,
        #      "Position:", position, "MarketPrice:", marketPrice, "MarketValue:", marketValue, "AverageCost:", averageCost,
        #      "UnrealizedPNL:", unrealizedPNL, "RealizedPNL:", realizedPNL, "AccountName:", accountName)

    def updateAccountValue(self, key: str, val: str, currency: str, accountName: str):
        if key == 'CashBalance' and currency == 'USD':
            self.balanceInUSD = val
        elif key == 'CashBalance' and currency == 'CAD':
            self.balanceInCAD = val
        #print("UpdateAccountValue. Key:", key, "Value:", val, "Currency:", currency, "AccountName:", accountName)

    #def updateAccountTime(self, timeStamp: str):
        #print("UpdateAccountTime. Time:", timeStamp)

    #def accountDownloadEnd(self, accountName: str):
        #print("AccountDownloadEnd. Account:", accountName)

    def start(self):
        # Account number can be omitted when using reqAccountUpdates with single account structure
        self.reqAccountUpdates(True, "")

    def stop(self):
        self.reqAccountUpdates(False, "")
        self.done = True
        self.disconnect()

def getBalanceInUSD() -> float:
	app = AccountApi()
	app.connect("127.0.0.1", 7497, 0)
	Timer(5, app.stop).start()
	app.run()
    
	return float(app.balanceInUSD)

def getBalanceInCAD() -> float:
	app = AccountApi()
	app.connect("127.0.0.1", 7497, 0)
	Timer(5, app.stop).start()
	app.run()
    
	return float(app.balanceInCAD)