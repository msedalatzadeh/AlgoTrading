from ibapi.client import *
from ibapi.wrapper import *
import sys; sys.path.append('/Users/sajjadedalatzadeh/GitHub/AlgoTrading')
from utility import price, account
import numpy as np
import time

class OrderApi(EClient, EWrapper):
  def __init__(self, type: str, action: str, ticker: str, qunatity: int = None, price: Decimal = None):
    EClient.__init__(self, self)
    self.type = type
    self.action = action
    self.price = price
    self.qunatity = qunatity
    self.ticker = ticker
    self.balance = None
    self.stockPrice = None
    self.avgFillPrice = None

  def nextValidId(self, orderId: OrderId):
    contract = Contract()
    contract.symbol = self.ticker
    contract.secType = "STK"    
    contract.exchange = "SMART" #"TSE"
    contract.currency = "USD"   #"CAD" 

    self.reqContractDetails(orderId, contract)

  def contractDetails(self, reqId: int, contractDetails: ContractDetails):
    print(contractDetails.contract)

    order = Order()
    order.orderId = reqId
    order.action = self.action
    order.orderType = self.type
    if self.qunatity:
        order.totalQuantity = self.qunatity
    elif self.action == 'BUY':
        self.balance = account.getBalanceInUSD()
        self.stockPrice = price.getStockPrice(self.ticker)
        order.totalQuantity = int(np.floor(self.balance * 0.95 / self.stockPrice))
    #elif self.action == 'SELL':
        # order.totalQuantity = account.getOwnedShares(self.ticker) # tech debt

    if self.type == 'LMT':
        order.tif = 'GTC'
        if self.price:
            order.lmtPrice = self.price
        else: 
            self.stockPrice = price.getStockPrice(self.ticker)
            if self.action == 'SELL':
              order.lmtPrice = round(self.stockPrice * 0.998, 2)
            else: #self.action == 'BUY'
              order.lmtPrice = round(self.stockPrice * 1.002, 2)
      
    self.placeOrder(order.orderId, contractDetails.contract, order)

  def openOrder(self, orderId: OrderId, contract: Contract, order: Order, orderState: OrderState):
    print(f"openOrder. orderId: {orderId}, contract: {contract}, order: {order}")

  def orderStatus(self, orderId: OrderId, status: str, filled: Decimal, remaining: Decimal, avgFillPrice: float, permId: int, parentId: int, lastFillPrice: float, clientId: int, whyHeld: str, mktCapPrice: float):
    self.avgFillPrice = avgFillPrice
    print(f"orderId: {orderId}, status: {status}, filled: {filled}, remaining: {remaining}, avgFillPrice: {avgFillPrice}, permId: {permId}, parentId: {parentId}, lastFillPrice: {lastFillPrice}, clientId: {clientId}, whyHeld: {whyHeld}, mktCapPrice: {mktCapPrice}")

  def execDetails(self, reqId: int, contract: Contract, execution: Execution):
    print(f"reqId: {reqId}, contract: {contract}, execution: {execution}")

def submitOrder(type: str, action: str, ticker: str, qunatity: int = None, price: Decimal = None):
    app = OrderApi(type, action, ticker, qunatity, price)
    app.connect("127.0.0.1", 7497, 100)
    app.run()

    time.sleep(10)
    app.disconnect()
    
    return app.avgFillPrice