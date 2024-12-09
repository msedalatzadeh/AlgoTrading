def getAvailableTickets():
    from ibapi.ticktype import TickTypeEnum

    for i in range(91):
	    print(TickTypeEnum.toStr(i), i)