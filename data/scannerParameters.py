from ibapi.client import EClient
from ibapi.wrapper import EWrapper

class TradeApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def scannerParameters(self, xml):
        super().scannerParameters(xml)
        open('scanner_params.xml', 'w').write(xml)
        print("ScannerParameters received.")

def websocket_con():
    app.run()

app = TradeApp()
app.connect(host='127.0.0.1', port=7496, clientId=23)

app.reqScannerParameters()
app.run()