from ibapi.client import EClient
from ibapi.wrapper import EWrapper

class ScannerApi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.topLosers = []

    def scannerData(self, reqId, rank, contractDetails, distance, benchmark, projection, legsStr):
        #super().scannerData(reqId, rank, contractDetails, distance, benchmark, projection, legsStr)
        self.topLosers.append(contractDetails.contract.symbol)

    def scannerDataEnd(self, reqId):
        self.cancelScannerSubscription(reqId)
        self.disconnect()