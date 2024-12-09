from ibapi.client import EClient
from ibapi.wrapper import EWrapper  
import time 

class IBapi(EWrapper, EClient):
     def __init__(self):
         EClient.__init__(self, self) 

def testApi():
    app = IBapi()
    app.connect('127.0.0.1', 7497, 123)
    app.run()

    time.sleep(2)
    app.disconnect()