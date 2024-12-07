from ibapi.client import *
from ibapi.wrapper import *

class OrderApi(EClient, EWrapper):
  def __init__(self, type: str, action: str, ticker: str, qunatity: int, price: Decimal = None):
    EClient.__init__(self, self)
    self.type = type
    self.action = action
    self.price = price
    self.qunatity = qunatity
    self.ticker = ticker

  def nextValidId(self, orderId: OrderId):
    contract = Contract()
    contract.symbol = self.ticker
    contract.secType = "STK"    
    contract.exchange = "SMART"
    contract.currency = "USD"

    self.reqContractDetails(orderId, contract)

  def contractDetails(self, reqId: int, contractDetails: ContractDetails):
    print(contractDetails.contract)

    order = Order()
    order.orderId = reqId
    order.action = self.action
    order.orderType = self.type
    order.totalQuantity = self.qunatity
    if self.type == 'LMT':
      order.lmtPrice = self.price
      order.tif = 'GTC'
      
    self.placeOrder(order.orderId, contractDetails.contract, order)

  def openOrder(self, orderId: OrderId, contract: Contract, order: Order, orderState: OrderState):
    print(f"openOrder. orderId: {orderId}, contract: {contract}, order: {order}")

  def orderStatus(self, orderId: OrderId, status: str, filled: Decimal, remaining: Decimal, avgFillPrice: float, permId: int, parentId: int, lastFillPrice: float, clientId: int, whyHeld: str, mktCapPrice: float):
    print(f"orderId: {orderId}, status: {status}, filled: {filled}, remaining: {remaining}, avgFillPrice: {avgFillPrice}, permId: {permId}, parentId: {parentId}, lastFillPrice: {lastFillPrice}, clientId: {clientId}, whyHeld: {whyHeld}, mktCapPrice: {mktCapPrice}")

  def execDetails(self, reqId: int, contract: Contract, execution: Execution):
    print(f"reqId: {reqId}, contract: {contract}, execution: {execution}")

def submitOrder(type: str, action: str, qunatity: int, price: Decimal = None):
    app = OrderApi(type, action, qunatity, price)
    app.connect("127.0.0.1", 7497, 100)
    app.run()

def test():
  print('test is working')