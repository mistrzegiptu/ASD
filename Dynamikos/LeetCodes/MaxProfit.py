def maxProfit(prices):
    n = len(prices)
    best = 0
    buy = prices[0]

    for i in range(n):
        if prices[i] < buy:
            buy = prices[i]
        else:
            best = max(best, prices[i] - buy)

    return best