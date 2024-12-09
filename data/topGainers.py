from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.scanner import ScannerSubscription
import time
import threading

class TradeApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def scannerData(self, reqId, rank, contractDetails, distance, benchmark, projection, legsStr):
        super().scannerData(reqId, rank, contractDetails, distance, benchmark, projection, legsStr)
        print(contractDetails.contract.symbol)

def usStkScan(asset_type="STK", asset_loc="STK.US.MAJOR", scan_code="TOP_PERC_GAIN"):
    scanSub = ScannerSubscription()
    scanSub.numberOfRows = 50
    scanSub.abovePrice = 10
    scanSub.belowPrice = 200
    scanSub.aboveVolume = 1000000
    scanSub.instrument = asset_type
    scanSub.locationCode = asset_loc
    scanSub.scanCode = scan_code
    return scanSub

def websocket_con():
    app.run()

app = TradeApp()
app.connect(host='127.0.0.1', port=7496, clientId=23)
con_thread = threading.Thread(target=websocket_con)
con_thread.start()

time.sleep(1)  # some latency added to ensure that the connection is established
app.reqScannerSubscription(1, usStkScan(), [], [])