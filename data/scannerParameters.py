from ibapi.client import EClient
from ibapi.wrapper import EWrapper

class ScannerApi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId):
        return self.reqScannerParameters()
    
    def scannerParameters(self, xml):
        dir = './data/scanner.xml'
        open(dir, 'w').write(xml)
        print("Scanner Parameters received.")

def saveToFile():
    def websocket_con():
        app.run()

    app = ScannerApi()
    app.connect(host='127.0.0.1', port=7497, clientId=23)
    app.run()