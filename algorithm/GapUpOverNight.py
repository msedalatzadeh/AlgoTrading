from ibapi.client import *
from ibapi.wrapper import *
from ..utility.Order import test
from datetime import datetime
import time

while True:
    now = datetime.now()
    if now.hour>=15 and now.minute>=56:
        #submitOrder('MKT', 'BUY', 'GWRE', 4)
        test()
        break
    
    time.sleep(60)