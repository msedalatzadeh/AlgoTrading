
import sys; sys.path.append('/Users/sajjadedalatzadeh/GitHub/AlgoTrading')
from data import scanner
from ibapi.scanner import ScannerSubscription
import time
import threading

def __usStkScan__(count: int):
    scanSub = ScannerSubscription()
    scanSub.numberOfRows = count
    scanSub.abovePrice = 5
    scanSub.belowPrice = 1000
    scanSub.aboveVolume = 2*10**6
    scanSub.instrument = "STK"
    scanSub.locationCode = "STK.US.MAJOR"
    scanSub.scanCode = "TOP_PERC_LOSE"
    return scanSub

def get(count: int) -> list[str]:
    app = scanner.ScannerApi()
    app.connect(host='127.0.0.1', port=7497, clientId=23)
    con_thread = threading.Thread(target=app.run)
    con_thread.start()

    time.sleep(1)  # some latency added to ensure that the connection is established
    app.reqScannerSubscription(1, __usStkScan__(count), [], [])
    time.sleep(10)
    print(app.topLosers)
    return app.topLosers