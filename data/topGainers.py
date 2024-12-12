import sys; sys.path.append('/Users/sajjadedalatzadeh/GitHub/AlgoTrading')
from data import scanner
from ibapi.scanner import ScannerSubscription
import time
import threading

def usStkScan():
    scanSub = ScannerSubscription()
    scanSub.numberOfRows = 5
    scanSub.abovePrice = 5
    scanSub.belowPrice = 1000
    scanSub.aboveVolume = 2*10**6
    scanSub.instrument = "STK"
    scanSub.locationCode = "STK.US.MAJOR"
    scanSub.scanCode = "TOP_PERC_GAIN"
    return scanSub

def get() -> list[str]:
    app = scanner.ScannerApi()
    app.connect(host='127.0.0.1', port=7497, clientId=23)
    con_thread = threading.Thread(target=app.run)
    con_thread.start()

    time.sleep(1)  # some latency added to ensure that the connection is established
    app.reqScannerSubscription(1, usStkScan(), [], [])
    time.sleep(10)
    print(app.topGainer)
    app.disconnect()
    return app.topGainer