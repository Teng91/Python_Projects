import numpy as np
 
def myAction01(priceMat, transFeeRate):
    cash = 1000
    hold = 0
    # user definition
    nextDay = 1
    dataLen, stockCount = priceMat.shape  # day size & stock count   
    stockHolding = np.zeros((dataLen,stockCount))  # Mat of stock holdings
    actionMat = []  # An k-by-4 action matrix which holds k transaction records.
 
    day = 0 ##初始化day為第一天
    while day < dataLen-nextDay:
        dayPrices = priceMat[day]  # Today price of each stock
        nextDayPrices = priceMat[ day + nextDay ]  # Next day price of each stock
 
        if day > 0:
            stockHolding[day] = stockHolding[day-1]  # The stock holding from the previous action day
 
        buyStock = -1  # which stock should buy. No action when is -1
        buyPrice = 0  # use how much cash to buy
        sellStock = []  # which stock should sell. No action when is null
        sellPrice = []  # get how much cash from sell
        bestPriceDiff = 0  # difference in today price & next day price of "buy" stock
        stockCurrentPrice = 0  # The current price of "buy" stock
 
 
 
 
 
        # Check next day price to "sell"
        for stock in range(stockCount) :
            todayPrice = dayPrices[stock]  # Today price
            nextDayPrice = nextDayPrices[stock]  # Next day price
            holding = stockHolding[day][stock]  # how much stock you are holding
 
 
 
            if holding > 0 :  # "sell" only when you have stock holding
                while nextDayPrice > todayPrice*(1+transFeeRate) and  day+1<dataLen: ##找出連續漲的最後一天，
                    day = day+1 ##繼續漲就繼續找下一天
                    nextDayPrice = priceMat[ day ][stock] ##價錢也更改為下一天
                ##找到了
                sellStock.append(stock)
                # "Sell"
                sellPrice.append(holding * todayPrice)
                cash = holding * todayPrice*(1-transFeeRate) # Sell stock to have cash
                stockHolding[day][stock] = 0 ##此時的day已經是最後漲的那天
                #stockHolding[day][sellStock] = 0 ##此時的day已經是最後漲的那天
 
 
 
        # Check next day price to "buy"
        if cash > 0 :  # "buy" only when you have cash
            for stock in range(stockCount) :
                todayPrice = dayPrices[stock]  # Today price
                nextDayPrice = nextDayPrices[stock]  # Next day price
 
 
                while nextDayPrice < todayPrice*(1+transFeeRate) and  day+1<dataLen: ##找出連續跌的最後一天，
                    day = day+1 ##繼續跌就繼續找下一天
                    nextDayPrice = priceMat[ day ][stock] ##價錢也更改為下一天
                ##找到了  
                diff = nextDayPrice - todayPrice*(1+transFeeRate)
                if diff > bestPriceDiff :  # this stock is better
                    bestPriceDiff = diff
                    buyStock = stock
                    stockCurrentPrice = todayPrice
 
 
            # "Buy" the best stock
            if buyStock >= 0 :
                buyPrice = cash
                stockHolding[day][buyStock] = cash*(1-transFeeRate) / stockCurrentPrice # Buy stock using cash
                cash = 0
 
        if day+1<dataLen:
            day = day+1 ##完事要記得加一才不會無限迴圈
 
 
        #########如果到最後一天要把他全賣掉唷
        if day == dataLen:
            for stock in range(stockCount) :
                todayPrice = dayPrices[stock]  # Today price
                nextDayPrice = nextDayPrices[stock]  # Next day price
                holding = stockHolding[day][stock]  # how much stock you are holding
                if holding > 0 :
                    sellStock.append(stock)
                    # "Sell"
                    sellPrice.append(holding * todayPrice)
                    cash = holding * todayPrice*(1-transFeeRate) # Sell stock to have cash
                    stockHolding[day][sellStock] = 0 ##此時的day已經是最後漲的那天
        ################################
 
 
 
 
        # Save your action this day
        if buyStock >= 0 or len(sellStock) > 0 :
            action = []
            if len(sellStock) > 0 :
                for i in range( len(sellStock) ) :
                    action = [day, sellStock[i], -1, sellPrice[i]]
                    actionMat.append( action )
            if buyStock >= 0 :
                action = [day, -1, buyStock, buyPrice]
                actionMat.append( action )
    return actionMat
