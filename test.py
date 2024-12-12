from utility import order
from ai import sentiment
from data import scannerParameters, topLosers, topGainers
from algorithm import gapUpOverNight
from utility import price, order

################
# test sentiment
# sentiment.getSentiment('MRNA')

##############
# test scanner
## scannerParameters.saveToFile()

########################
# test top losers/gainer
## topLosers.get()
## topGainers.get()

####################
# test gapUpOverNight algorithm
gapUpOverNight.implement()

############
# test price
##p = price.getStockPrice('TSLA') # this need some optimization
##print("price is: ", p)

#########
# submit order
## order.submitOrder('MKT', 'SELL', 'GOOGL', 35)