def maxProfit(prices):
    """Sets a pointer at index 0 to start as our lowest value
    Iterates through prices, if a price is found to be lower than lowest
    lowest will be re-assigned to that price
    profit is initialized to 0
    On each iteration we check if the current highest profit is higher than
    the current price - our current lowest price
    returns: maximum profit if bought and sold at the best time"""
    lowest = prices[0]
    profit = 0
    for price in prices:
        if price < lowest:
            lowest = price
        profit = max(profit, price-lowest)
    return profit

print(maxProfit([7,1,5,3,6,4])) #=> 5
print(maxProfit([7,6,4,3,1])) #=> 0 no transactions done (descending order)
